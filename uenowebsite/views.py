from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from uenowebsite.models import Category
from uenowebsite.models import Page
from django.templatetags.static import static
from collections import defaultdict

from uenowebsite.models import Product, Building
from uenowebsite.forms import CategoryForm, EnquiryForm, PageForm



def index(request):
    category_list = Category.objects.all()
    products = Product.objects.all()
    buildings = Building.objects.all().order_by('series', 'name')
    
    grouped_buildings = defaultdict(list)
    for building in buildings:
        grouped_buildings[building.series].append(building)
    
    context_dict = {
        'boldmessage': 'Welcome to Ueno Corporation – Global Trading Excellence!',
        'categories': category_list,
        'products': products,
        'grouped_buildings': dict(grouped_buildings),  # Convert to regular dict for template
    }
    
    return render(request, 'uenowebsite/index.html', context=context_dict)


def about(request):
    context_dict = {'boldmessage': 'Here is the about page.'}
    return render(request, 'uenowebsite/about.html', context=context_dict)

def show_category(request, category_name_slug):
    # Create a context dictionary to pass data to the template
    context_dict = {}

    try:
        # Attempt to retrieve the category based on the slug
        category = Category.objects.get(slug=category_name_slug)

        # Retrieve all associated pages for the category
        pages = Page.objects.filter(category=category)

        # Add category and pages to the context dictionary
        context_dict['category'] = category
        context_dict['pages'] = pages
    except Category.DoesNotExist:
        # If category is not found, set to None so template can handle it gracefully
        context_dict['category'] = None
        context_dict['pages'] = None

    # Render the response and return it
    return render(request, 'uenowebsite/category.html', context=context_dict)

def add_category(request):
    form = CategoryForm()

    # A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Redirect to the index page after saving.
            return redirect('uenowebsite:index')
        else:
            # Print form errors to the console.
            print(form.errors)

    # Render the form (whether it's a GET request or invalid POST)
    return render(request, 'uenowebsite/add_category.html', {'form': form})

def enquiry(request):
    if request.method == 'POST':
        # If the form is submitted, populate the form with POST data
        form = EnquiryForm(request.POST)
        
        # Check if the form is valid
        if form.is_valid():
            # Save the enquiry data into the database
            form.save()
            
            # Show a success message after submission
            return render(request, 'uenowebsite/enquiry.html', {
                'form': form,
                'message': 'Thank you for your enquiry! We will get back to you soon.'
            })
        else:
            # If the form is invalid, you can print the errors (or handle them in a more user-friendly way)
            print(form.errors)
    else:
        # For a GET request, just show an empty form
        form = EnquiryForm()

    # Render the enquiry form on the page
    return render(request, 'uenowebsite/enquiry.html', {'form': form})

def add_page(request, category_name_slug):

    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None

    if category is None:
        return redirect('/uenowebsite/')

    form = PageForm()

    if request.method == 'POST':
        form = PageForm(request.POST)

        if form.is_valid():
            page = form.save(commit=False)  # Don't save the page yet
            page.category = category  # Assign the category to the page
            page.save()  # Save the page to the database

            # Redirect to the category page after saving the page
            return redirect(reverse('uenowebsite:show_category', kwargs={'category_name_slug': category_name_slug}))
        else:
            # Print errors to the terminal for debugging
            print(form.errors)

    # Render the form along with the category details
    context_dict = {'form': form, 'category': category}
    return render(request, 'uenowebsite/add_page.html', context=context_dict)

def faq_view(request):
    contact_url = reverse('uenowebsite:enquiry')
    catalogue_url = static('docs/UENO PRODUCT CATALOGUE.pdf')

    faqs = [
        ("We would like to meet with you to discuss a product.",
         f'We’d be happy to arrange a meeting. Please <a href="{contact_url}">contact us</a> with your preferred date, time, and the product you’d like to discuss.'),

        ("Can we get an offer regarding a product you offer?",
         f'Absolutely. Please let us know the specific product, quantity, and delivery destination via our <a href="{contact_url}">enquiry form</a>, and we will send you a tailored offer.'),

        ("Do you export to [specific country]?",
         f'We export globally, depending on the product category and shipping conditions. To confirm availability for your country, please <a href="{contact_url}">get in touch with us</a>.'),

        ("Can we receive a full product catalog?",
         f'Yes. You can download our catalogue <a href="{catalogue_url}" target="_blank" rel="noopener noreferrer">here</a>. If you need a printed version, please request it via our <a href="{contact_url}">contact page</a>.'),

        ("How can we discuss pricing, quantity, and conditions?",
         f'Pricing and conditions vary depending on the product, quantity, and shipping destination. Please share your requirements via our <a href="{contact_url}">enquiry form</a>, and we’ll follow up with detailed information.'),

        ("What are your payment terms?",
         f'Payment terms depend on the product category, order volume, and buyer location. For accurate details, please <a href="{contact_url}">contact us</a> with your inquiry.'),

        ("What is the estimated delivery time for orders?",
         f'Delivery times vary based on the destination, item availability, and shipping method. We will provide an estimate once we receive your product inquiry via the <a href="{contact_url}">enquiry form</a>.'),
    ]

    return render(request, 'uenowebsite/faq.html', {'faqs': faqs})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'uenowebsite/product_detail.html', {'product': product})

def president_message(request):
    return render(request, 'uenowebsite/president_message.html')
