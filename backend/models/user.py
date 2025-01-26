from datetime import datetime, UTC
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Text, Table
from sqlalchemy.ext.associationproxy import AssociationProxy, association_proxy
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


# Таблица ассоциации
class UserRole(Base):
    __tablename__ = "user_roles"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"), primary_key=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now(UTC))

    # Relationships
    user: Mapped["User"] = relationship(back_populates="role_links")
    role: Mapped["Role"] = relationship(back_populates="user_links")


class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(150), unique=True)
    description: Mapped[str | None] = mapped_column(Text)

    # Relationships
    user_links: Mapped[list["UserRole"]] = relationship(back_populates="role")

    # Association proxy (прямой доступ к пользователям через роль)
    users: AssociationProxy[list["User"]] = association_proxy("user_links", "user")


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    hashed_password: Mapped[str]
    name: Mapped[str | None] = mapped_column(String(255))
    last_name: Mapped[str | None] = mapped_column(String(255))
    phone_number: Mapped[str | None] = mapped_column(String(80))
    two_number: Mapped[str | None] = mapped_column(String(80))
    is_active: Mapped[bool] = mapped_column(default=True)
    is_superuser: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(UTC))

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC),
    )

    # Relationships
    role_links: Mapped[list["UserRole"]] = relationship(back_populates="user")

    # Association proxy (прямой доступ к ролям через пользователя)
    roles: AssociationProxy[list["Role"]] = association_proxy("role_links", "role")
