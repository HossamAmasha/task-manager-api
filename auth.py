from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlmodel import Session, select

from database import engine
from models import User, UserCreate, Token , UserPublic
from security import hash_password, verify_password, create_access_token, decode_access_token


router = APIRouter(prefix="/api/v1/auth", tags=["Authentication"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

@router.post("/register")
def register(user: UserCreate):
    with Session(engine) as session:
        existing_user = session.exec(
            select(User).where(User.username == user.username)
        ).first()

        if existing_user:
            raise HTTPException(status_code=400, detail="Username already exists")

        new_user = User(
            username=user.username,
            hashed_password=hash_password(user.password)
        )

        session.add(new_user)
        session.commit()
        session.refresh(new_user)

        return {"message": "User registered successfully"}

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    with Session(engine) as session:
        user = session.exec(
            select(User).where(User.username == form_data.username)
        ).first()

        if not user or not verify_password(form_data.password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid username or password"
            )

        access_token = create_access_token(data={"sub": user.username})

        return {
            "access_token": access_token,
            "token_type": "bearer"
        }
    



def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail= "Could not validate credentials"
    )

    payload = decode_access_token(token)

    if payload is None:
        raise credentials_exception
    
    username = payload.get("sub")
    if username is None:
        raise credentials_exception
    
    with Session(engine) as session:
        user = session.exec(
            select(User).where(User.username == username)
        ).first()

        if user is None:
            raise credentials_exception
        
        return user
    

@router.get("/me", response_model=UserPublic)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user