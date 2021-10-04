from api.models.family import Family
from django.urls import path
from .views.family_views import Families, FamilyDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword, Index
# from .views.parent_views import Parents, ParentDetail


urlpatterns = [
  	# Restful routing
    path('families/', Families.as_view(), name='families'),
    path('families/<int:pk>/', FamilyDetail.as_view(), name='family_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw'),
    path('index/', Index.as_view(), name='index')
    # path('parents', Parents.as_view(), name='parents'),
    # path('parents/<int:pk>', ParentDetail.as_view(), name='parent_detail'),
]
