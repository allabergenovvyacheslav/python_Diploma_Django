from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .forms import ContactForm
from .models import Product, Category

# Create your views here.

# Представление для главной страницы
def home(request):
    # Получаем все категории
    categories = Category.objects.all()
    return render(request, 'catalog/home.html', {'categories': categories,})


# Создание представления для отображения списка товаров из БД
def product_list(request):
    products = Product.objects.all()  # Получаем все товары из базы данных
    return render(request, 'catalog/product_list.html', {'products': products})


# Создание представления для обработки формы
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено")
    else:
        form = ContactForm()
    return render(request, 'catalog/contact.html', {'form': form})




# products = [
#     {'id': 1, 'name': 'дуб натур 420х70х15', 'category': 'Штучный паркет', 'price': 2500},
#     {'id': 2, 'name': 'дуб селект 420х70х15', 'category': 'Штучный паркет', 'price': 3200},
#     {'id': 3, 'name': 'дуб рустик 420х70х15', 'category': 'Штучный паркет', 'price': 1900},
#     {'id': 4, 'name': 'дуб натур 900х90х15', 'category': 'Широкоформатный паркет', 'price': 3000},
#     {'id': 5, 'name': 'дуб селект 900х90х15', 'category': 'Широкоформатный паркет', 'price': 3900},
#     {'id': 6, 'name': 'дуб рустик 900х90х15', 'category': 'Широкоформатный паркет', 'price': 2300},
#     {'id': 7, 'name': 'Berger Eco Gold', 'category': 'Лак для паркета', 'price': 15000},
#     {'id': 8, 'name': 'Berger Ceramic Star', 'category': 'Лак для паркета', 'price': 20000},
#     {'id': 9, 'name': 'Korvicol MS Elastic', 'category': 'Клей для паркета', 'price': 5500},
#     {'id': 10, 'name': 'Korvicol 2KPU', 'category': 'Клей для паркета', 'price': 15000},
# ]
#
#
# def product_list(request):
#     # Получаем параметр 'category' из строки запроса
#     category = request.GET.get('category')
#
#     # Если категория указана, фильтруем товары
#     if category:
#         filtered_products = [product for product in products if product['category'] == category]
#     else:
#         filtered_products = products
#
#     # Передаем товары в шаблон
#     return render(request, 'catalog/product_list.html', {'products': filtered_products})
#
#
# def add_product(request):
#     if request.method == 'POST':
#
#         # Получаем данные из формы
#         name = request.POST.get('name')
#         category = request.POST.get('category')
#         price = request.POST.get('price')
#
#         # Добавляем новый товар в список
#         products.append(
#             {
#                 'id': len(products) + 1,
#                 'name': name,
#                 'category': category,
#                 'price': int(price),
#             }
#         )
#         # Перенаправляем на список товаров
#         return redirect('product_list')  # Имя маршрута списка товаров
#
#     # Если GET-запрос, отображаем форму
#     return render(request, 'catalog/add_product.html')
