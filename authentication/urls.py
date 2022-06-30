from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CustomUserRegisterViewSet,
    UpdatePassword,
    LogoutView,
    CardModelViewSet,
)
from rest_framework_simplejwt import views as jwt_views


router = DefaultRouter()
router.register(r"register", CustomUserRegisterViewSet, basename="register")
router.register(r"card", CardModelViewSet, basename="card")

urlpatterns = [
    path("", include(router.urls)),
    path("login/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("login/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    path("change-password/", UpdatePassword.as_view(), name="change-password"),
    path("logout/", LogoutView.as_view(), name="auth_logout"),
]
