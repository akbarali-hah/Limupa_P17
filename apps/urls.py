from django.contrib.auth.views import LogoutView
from django.urls import path, include
from apps.views import BlogListView, RegisterFormView, CustomLoginView, BlogDetailView, IndexView, ShopListView, \
    SingleProductView, SignUpToNewsView, UserUpdateView

urlpatterns = [
    path('', IndexView.as_view(), name='index_page'),
    path('register', RegisterFormView.as_view(), name='register_page'),
    path('login', CustomLoginView.as_view(), name='login_page'),
    path('logout', LogoutView.as_view(next_page='login_page'), name='logout_page'),
    path('profile/<pk>', UserUpdateView.as_view(), name='profile_update_page'),
    path('news-letter', SignUpToNewsView.as_view(), name='news_letter_page'),
    path('blog-list', BlogListView.as_view(), name='blog_list_page'),
    path('blog-detail/<uuid:pk>', BlogDetailView.as_view(), name='blog_detail_page'),
    path('shop-list', ShopListView.as_view(), name='shop_list_page'),
    path('product/<int:pk>', SingleProductView.as_view(), name='single_product_page'),
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
]
