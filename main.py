from pydantic import BaseModel, EmailStr, ValidationError, field_validator


class User(BaseModel):  # définition d'un modèle simple
    username: str
    email: EmailStr  # Utilisation d'un type spécial
    age: int

    @field_validator("age")  # Spécification du champ ciblé par le validateur
    def check_age(cls, v: int) -> int:
        if v < 0:
            raise ValueError("Must be a positive integer")
        if v < 18:
            raise ValueError("Must be at least 18 years old")
        return v


def main():
    print("Hello from pydantic-learning!")
    try:
        user = User(username="johndoe", email="john@example.com", age=25)
        print(user)
    except ValidationError as e:
        print(e.json())


if __name__ == "__main__":
    main()
