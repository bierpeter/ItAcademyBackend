from .models import User, Property
from django.http import HttpResponse
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404

def index(request):
    return render(request, 'index.html')

class LoginUserForm:
    def login(request):
        if request.POST:
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
        else:
            return render(request, 'login.html')
            
    def grant_access(request,user_id, is_admin=False):
        if request.GET:
            user = User.objects.get(id=user_id)
            if is_admin:
                user.is_staff = True
                user.is_superuser = True
            else:
                user.is_staff = False
                user.is_superuser = False
            user.save()
    
    def is_admin(user):
        if user.role == 'Администратор':
            return True

        
    def revoke_access(user_id):
        user = User.objects.get(id=user_id)
        user.role = 'user'
        user.save()
        
# This class is used to create and edit user by admin
class Users:
    def edit_User(request,self, user_id):
        def create_user(request):
            try:
                if request.PUT:
                    if User.role == 'admin':
                        email = request.PUT['email']
                        password = request.PUT['password']
                        firstName = request.PUT['firstName']
                        lastName = request.PUT['lastName']
                        role = request.PUT['role']
                        image = request.FILES['image']
                        user = User.objects.create_user(
                            email=email, 
                            password=password, 
                            first_name=firstName, 
                            last_name=lastName, 
                            role=role,
                            image=image
                        )
                        user.save()
                        return redirect('index')
                    else:
                        return HttpResponse(
                            f'''<h3>You are not authorized to create a user.
                            Please contact the admin or try again.<h3>'''
                        )
                else:
                    return render(request, 'create_user.html')
            except IntegrityError:
                return HttpResponse(
                    f'''<h3>User with this email already exists.<h3>'''
                )
            
        def delete_user(request):
            try:
                if request.DELETE:
                        if User.role == 'admin':
                            user_id = request.DELETE['user_id']
                            user = User.objects.get(id=user_id)
                            user.delete()
                            return redirect('index')
                        
                        else:
                            return HttpResponse(
                                f'''<h3>You are not authorized to delete a user.
                                Please contact the admin or try again.<h3>'''
                            )
            except User.UserDoesNotExist():
                return HttpResponse(
                    f'''<h3>User does not exist.<h3>'''
                )     
        if user_id == User.ID_User:
            if LoginUserForm.is_admin():
                if request.PUT:
                    return create_user(request)
                else:
                    return delete_user(request)
                
    def user_list(request):
        users = User.objects.all()  # Получаем всех пользователей
        context = {
            'users': users
        }
        return render(request, 'user_list.html', context)
    
    @login_required
    def user_profile_view(request, user_id):
        user = get_object_or_404(User, id=user_id)
        return render(request, 'user_profile.html', {'user': user})

                    
class Properties:
    def edit_Property(request,self, property_id):
        def create_property(request):
            try:
                if request.PUT:
                    if User.role == 'admin':
                        category = request.PUT['category']
                        image = request.FILES['image']
                        conditions = request.PUT['conditions']
                        building = request.PUT['building']
                        floor = request.PUT['floor']
                        room = request.PUT['room']
                        property = Property.objects.create(
                            category=category,
                            image=image,
                            conditions=conditions,
                            building=building,
                            floor=floor,
                            room=room
                        )
                        property.save()
                return redirect('index')
            except IntegrityError:
                return HttpResponse(
                    f'''<h3>Property with this category already exists.<h3>'''
                )
                
        def delete_property(request):
            try:
                if request.PUT:
                    if User.role == 'admin':
                        property_id = request.PUT['property_id']
                        property = Property.objects.get(id=property_id)
                    property.delete()
            except Property.DoesNotExist():
                return HttpResponse(
                    f'''<h3>Property does not exist.<h3>'''
                )
        if property_id == Property.ID_Property:
            if self.is_admin():
                if request.PUT:
                    return create_property(request)
                else:
                    return delete_property(request)



    # Экран выбора помещения (план корпуса)
    @login_required
    def select_view(request):
        scheme = Property.building
        return render(request, 'room_select.html', {'scheme': scheme})


    # Экран просмотра помещения
    @login_required
    def detail_view(request, room_id):
        room = get_object_or_404(Property, id=room_id)
        return render(request, 'room_detail.html', {'room': room})

    @user_passes_test(LoginUserForm.is_admin)
    def property_edit_view(request, property_id=None):
        if property_id:
            property_unit = get_object_or_404(Property, id=property_id)
        else:
            property_unit = None
        return render(request, 'property_edit.html', {'property': property_unit})

    # Каталог имущественного фонда
    @login_required
    def property_catalog_view(request):
        return render(request, 'property_catalog.html', {'properties': Property})