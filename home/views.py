from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView, PasswordResetConfirmView
from admin_tabler.forms import RegistrationForm, LoginForm, UserPasswordResetForm, UserSetPasswordForm, UserPasswordChangeForm
from django.contrib.auth import logout
from django.views.generic import CreateView
from django.http import JsonResponse
from django.db.utils import IntegrityError  # Import IntegrityError for error handling
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import UserAdditionalInfo
from .models import PlatformCategory
from .models import IncomeCategory
from .models import ExpenseCategory
from .models import SavingCategory
from .models import DebugCategory
from .models import IncomeExpenseData
from .models import AssetData
import datetime

@login_required
def index_template(request):
    context = {
        'parent': '',
        'segment': 'index'
    }
    return render(request, 'pages/index.html', context)

def index(request):

    user = request.user

    try:
        user_additional_info = UserAdditionalInfo.objects.get(user=user)
    except:
        user_additional_info = None

    context = {
        'parent': '',
        'segment': 'index',
        'userAdditionalInfo': user_additional_info,
    }
    return render(request, 'pages/index_finance_tracker.html', context)

# Interface
def accordion(request):
    context = {
        'parent': 'interface',
        'segment': 'accordion',
    }
    return render(request, 'pages/accordion.html', context)

def blank_page(request):
    context = {
        'parent': 'interface',
        'segment': 'blank_page',
    }
    return render(request, 'pages/blank.html', context)

def badges(request):
    context = {
        'parent': 'interface',
        'segment': 'badges',
    }
    return render(request, 'pages/badges.html', context)

def buttons(request):
    context = {
        'parent': 'interface',
        'segment': 'buttons',
    }
    return render(request, 'pages/buttons.html', context)

# Cards
def sample_cards(request):
    context = {
        'parent': 'interface',
        'segment': 'sample_cards',
    }
    return render(request, 'pages/cards.html', context)

def card_actions(request):
    context = {
        'parent': 'interface',
        'segment': 'card_actions',
    }
    return render(request, 'pages/card-actions.html', context)

def cards_masonry(request):
    context = {
        'parent': 'interface',
        'segment': 'cards_masonry',
    }
    return render(request, 'pages/cards-masonry.html', context)

def colors(request):
    context = {
        'parent': 'interface',
        'segment': 'colors',
    }
    return render(request, 'pages/colors.html', context)

def data_grid(request):
    context = {
        'parent': 'interface',
        'segment': 'data_grid',
    }
    return render(request, 'pages/datagrid.html', context)

def datatables(request):
    context = {
        'parent': 'interface',
        'segment': 'datatables',
    }
    return render(request, 'pages/datatables.html', context)

def dropdowns(request):
    context = {
        'parent': 'interface',
        'segment': 'dropdowns',
    }
    return render(request, 'pages/dropdowns.html', context)

def modals(request):
    context = {
        'parent': 'interface',
        'segment': 'modals',
    }
    return render(request, 'pages/modals.html', context)

def maps(request):
    context = {
        'parent': 'interface',
        'segment': 'maps',
    }
    return render(request, 'pages/maps.html', context)

def map_fullsize(request):
    context = {
        'parent': 'interface',
        'segment': 'map_fullsize',
    }
    return render(request, 'pages/map-fullsize.html', context)

def vector_maps(request):
    context = {
        'parent': 'interface',
        'segment': 'vector_maps',
    }
    return render(request, 'pages/maps-vector.html', context)

def navigation(request):
    context = {
        'parent': 'interface',
        'segment': 'navigation',
    }
    return render(request, 'pages/navigation.html', context)

def charts(request):
    context = {
        'parent': 'interface',
        'segment': 'charts',
    }
    return render(request, 'pages/charts.html', context)

def pagination(request):
    context = {
        'parent': 'interface',
        'segment': 'pagination',
    }
    return render(request, 'pages/pagination.html', context)

def placeholder(request):
    context = {
        'parent': 'interface',
        'segment': 'placeholder',
    }
    return render(request, 'pages/placeholder.html', context)

def steps(request):
    context = {
        'parent': 'interface',
        'segment': 'steps',
    }
    return render(request, 'pages/steps.html', context)

def stars_rating(request):
    context = {
        'parent': 'interface',
        'segment': 'stars_rating',
    }
    return render(request, 'pages/stars-rating.html', context)

def tabs(request):
    context = {
        'parent': 'interface',
        'segment': 'tabs',
    }
    return render(request, 'pages/tabs.html', context)

def tables(request):
    context = {
        'parent': 'interface',
        'segment': 'tables',
    }
    return render(request, 'pages/tables.html', context)

def carousel(request):
    context = {
        'parent': 'interface',
        'segment': 'carousel',
    }
    return render(request, 'pages/carousel.html', context)

def lists(request):
    context = {
        'parent': 'interface',
        'segment': 'lists',
    }
    return render(request, 'pages/lists.html', context)

def typography(request):
    context = {
        'parent': 'interface',
        'segment': 'typography',
    }
    return render(request, 'pages/typography.html', context)

def offcanvas(request):
    context = {
        'parent': 'interface',
        'segment': 'offcanvas',
    }
    return render(request, 'pages/offcanvas.html', context)

def markdown(request):
    context = {
        'parent': 'interface',
        'segment': 'markdown',
    }
    return render(request, 'pages/markdown.html', context)

def dropzone(request):
    context = {
        'parent': 'interface',
        'segment': 'dropzone',
    }
    return render(request, 'pages/dropzone.html', context)

def lightbox(request):
    context = {
        'parent': 'interface',
        'segment': 'lightbox',
    }
    return render(request, 'pages/lightbox.html', context)

def tinymce(request):
    context = {
        'parent': 'interface',
        'segment': 'tinymce',
    }
    return render(request, 'pages/tinymce.html', context)

def inline_player(request):
    context = {
        'parent': 'interface',
        'segment': 'inline_player',
    }
    return render(request, 'pages/inline-player.html', context)


# Authentication
class RegistrationView(CreateView):
  template_name = 'pages/sign-up.html'
  form_class = RegistrationForm
  success_url = '/accounts/login/'

class LoginView(LoginView):
  template_name = 'pages/sign-in.html'
  form_class = LoginForm

class LoginViewIllustrator(LoginView):
  template_name = 'pages/sign-in-illustration.html'
  form_class = LoginForm

class LoginViewCover(LoginView):
  template_name = 'pages/sign-in-cover.html'
  form_class = LoginForm

def logout_view(request):
    logout(request)
    return redirect('/accounts/login/')

def login_link(request):
    return render(request, 'pages/sign-in-link.html')

class PasswordReset(PasswordResetView):
  template_name = 'pages/forgot-password.html'
  form_class = UserPasswordResetForm

class UserPasswordResetConfirmView(PasswordResetConfirmView):
  template_name = 'pages/password-reset-confirm.html'
  form_class = UserSetPasswordForm

class UserPasswordChangeView(PasswordChangeView):
  template_name = 'pages/password-change.html'
  form_class = UserPasswordChangeForm

def terms_service(request):
    return render(request, 'pages/terms-of-service.html')

def lock_screen(request):
    return render(request, 'pages/auth-lock.html')

# Error and maintenance
def error_404(request):
    return render(request, 'pages/error-404.html')

def error_500(request):
    return render(request, 'pages/error-500.html')

def maintenance(request):
    return render(request, 'pages/error-maintenance.html')


def form_elements(request):
    context = {
        'parent': '',
        'segment': 'form_elements',
    }
    return render(request, 'pages/form-elements.html', context)

# Extra
def empty_page(request):
    context = {
        'parent': 'extra',
        'segment': 'empty_page',
    }
    return render(request, 'pages/empty.html', context)

def cookie_banner(request):
    context = {
        'parent': 'extra',
        'segment': 'cookie_banner',
    }
    return render(request, 'pages/cookie-banner.html', context)

def activity(request):
    context = {
        'parent': 'extra',
        'segment': 'activity',
    }
    return render(request, 'pages/activity.html', context)

def gallery(request):
    context = {
        'parent': 'extra',
        'segment': 'gallery',
    }
    return render(request, 'pages/gallery.html', context)

def invoice(request):
    context = {
        'parent': 'extra',
        'segment': 'invoice',
    }
    return render(request, 'pages/invoice.html', context)

def search_results(request):
    context = {
        'parent': 'extra',
        'segment': 'search_results',
    }
    return render(request, 'pages/search-results.html', context)

def pricing_cards(request):
    context = {
        'parent': 'extra',
        'segment': 'pricing_cards',
    }
    return render(request, 'pages/pricing.html', context)

def pricing_table(request):
    context = {
        'parent': 'extra',
        'segment': 'pricing_table',
    }
    return render(request, 'pages/pricing-table.html', context)

def faq(request):
    context = {
        'parent': 'extra',
        'segment': 'faq',
    }
    return render(request, 'pages/faq.html', context)

def users(request):
    context = {
        'parent': 'extra',
        'segment': 'users',
    }
    return render(request, 'pages/users.html', context)

def license(request):
    context = {
        'parent': 'extra',
        'segment': 'license',
    }
    return render(request, 'pages/license.html', context)

def logs(request):
    context = {
        'parent': 'extra',
        'segment': 'logs',
    }
    return render(request, 'pages/logs.html', context)

def music(request):
    context = {
        'parent': 'extra',
        'segment': 'music',
    }
    return render(request, 'pages/music.html', context)

def photogrid(request):
    context = {
        'parent': 'extra',
        'segment': 'photogrid',
    }
    return render(request, 'pages/photogrid.html', context)

def tasks(request):
    context = {
        'parent': 'extra',
        'segment': 'tasks',
    }
    return render(request, 'pages/tasks.html', context)

def uptime(request):
    context = {
        'parent': 'extra',
        'segment': 'uptime',
    }
    return render(request, 'pages/uptime.html', context)

def widgets(request):
    context = {
        'parent': 'extra',
        'segment': 'widgets',
    }
    return render(request, 'pages/widgets.html', context)

def wizard(request):
    context = {
        'parent': 'extra',
        'segment': 'widgets',
    }
    return render(request, 'pages/wizard.html', context)

def settings(request):
    user = request.user
    user_id= request.user.id

    if request.method == 'GET': # When load the URL first time

        try:
            user_additional_info = UserAdditionalInfo.objects.get(user=user)
        except:
            user_additional_info = None

        print(user_additional_info)
        
        context = {
            'parent': 'extra',
            'segment': 'settings',
            'userAdditionalInfo': user_additional_info,
        }
        return render(request, 'pages/settings.html', context)
    
    else: 
        if 'update_user' == request.POST.get('action', None):
            updateObject = request.POST.get('updateObject', None)
            updateValue = request.POST.get('updateValue', None)

            record = User.objects.get(id=int(user_id))
            
            match updateObject:
                case 'email':
                    record.email = updateValue

            try:
                record.save() 
                return JsonResponse({'Success': 'Updated'}, status=200)
                #return JsonResponse(status=200)

            except IntegrityError as e:
                print(f'Error: {e}')  # Print the specific IntegrityError for debugging
                return JsonResponse({'Error': 'Cannot pass new object(s) to the model'}, status=400)
        
        else: #('update_userAdditionalInfo' == request.POST.get('action', None)) or ('delete_userAdditionalInfo' == request.POST.get('action', None)) :
            action = request.POST.get('action', None)
            updateObject = request.POST.get('updateObject', None)
            inputType = request.POST.get('inputType', None)

            if 'update_userAdditionalInfo' == action:
                if 'file' == inputType:
                    updateFile = request.FILES.get('updateFile', None)
                else: #'info' == inputType:
                    updateValue = request.POST.get('updateValue', None)

            try:
                record = UserAdditionalInfo.objects.get(user=user)
            except:
                record = None

            if record: #UserAdditionalInfo exists
                match updateObject:
                    case 'changeProfilePicture':
                        record.profilePicture = updateFile
                    case 'deleteProfilePicture':
                        record.profilePicture = None
                try:
                    record.save() 

                    # Serialize the record data before returning it in JsonResponse
                    match updateObject:
                        case 'changeProfilePicture':
                            serialized_data = {
                                'profilePicture': record.profilePicture.url,
                            }
                            
                        case 'deleteProfilePicture':
                            serialized_data = None

                    return JsonResponse({'data': serialized_data}, status=200)

                except IntegrityError as e:
                    print(f'Error: {e}')  # Print the specific IntegrityError for debugging
                    return JsonResponse({'Error': 'Cannot pass new object(s) to the model'}, status=400)

            else: #UserAdditionalInfo doesn't exist
                if 'update_userAdditionalInfo' == action:
                   
                    match updateObject:
                        case 'changeProfilePicture':
                            record = UserAdditionalInfo.objects.create(
                                user=user,
                                profilePicture=updateFile,
                            )
                            
                    try:
                        record.save()
                        print('Saved new item')
                        # Serialize the record data before returning it in JsonResponse
                        serialized_data = {
                            'profilePicture': record.profilePicture.url,
                        }
                        return JsonResponse({'data': serialized_data})
                        #return JsonResponse({'data': 'ddd'})

                    except IntegrityError as e:
                        print(f'Error: {e}')  # Print the specific IntegrityError for debugging
                        return JsonResponse({'Error': 'Cannot pass new object(s) to the model'}, status=400)
                
                else: #'delete_userAdditionalInfo' == action:
                    print("Do nothing as no user found in the model")
                    return JsonResponse({'Success':'Do nothing as no user found in the model'}, status=200)

            
            

def settings_plan(request):
    context = {
        'parent': 'extra',
        'segment': 'settings',
    }
    return render(request, 'pages/settings-plan.html', context)

def trial_ended(request):
    context = {
        'parent': 'extra',
        'segment': 'trial_ended',
    }
    return render(request, 'pages/trial-ended.html', context)

def job_listing(request):
    context = {
        'parent': 'extra',
        'segment': 'job_listing',
    }
    return render(request, 'pages/job-listing.html', context)

def page_loader(request):
    context = {
        'parent': 'extra',
        'segment': 'page_loader',
    }
    return render(request, 'pages/page-loader.html', context)

# Layout
def layout_horizontal(request):
    context = {
        'parent': 'layout',
        'segment': 'layout_horizontal',
    }
    return render(request, 'pages/layout-horizontal.html', context)

def layout_boxed(request):
    context = {
        'parent': 'layout',
        'segment': 'layout_boxed',
    }
    return render(request, 'pages/layout-boxed.html', context)

def layout_vertical(request):
    context = {
        'parent': 'layout',
        'segment': 'layout_vertical',
    }
    return render(request, 'pages/layout-vertical.html', context)

def layout_vertical_transparent(request):
    context = {
        'parent': 'layout',
        'segment': 'layout_vertical_transparent',
    }
    return render(request, 'pages/layout-vertical-transparent.html', context)

def layout_vertical_right(request):
    context = {
        'parent': 'layout',
        'segment': 'layout_vertical_right',
    }
    return render(request, 'pages/layout-vertical-right.html', context)

def layout_condensed(request):
    context = {
        'parent': 'layout',
        'segment': 'layout_condensed',
    }
    return render(request, 'pages/layout-condensed.html', context)

def layout_combined(request):
    context = {
        'parent': 'layout',
        'segment': 'layout_combined',
    }
    return render(request, 'pages/layout-combo.html', context)

def layout_navbar_dark(request):
    context = {
        'parent': 'layout',
        'segment': 'layout_navbar_dark',
    }
    return render(request, 'pages/layout-navbar-dark.html', context)

def layout_navbar_sticky(request):
    context = {
        'parent': 'layout',
        'segment': 'layout_navbar_sticky',
    }
    return render(request, 'pages/layout-navbar-sticky.html', context)

def layout_navbar_overlap(request):
    context = {
        'parent': 'layout',
        'segment': 'layout_navbar_overlap',
    }
    return render(request, 'pages/layout-navbar-overlap.html', context)

def layout_rtl(request):
    context = {
        'parent': 'layout',
        'segment': 'layout_rtl',
    }
    return render(request, 'pages/layout-rtl.html', context)

def layout_fluid(request):
    context = {
        'parent': 'layout',
        'segment': 'layout_fluid',
    }
    return render(request, 'pages/layout-fluid.html', context)

def layout_fluid_vertical(request):
    context = {
        'parent': 'layout',
        'segment': 'layout_fluid_vertical',
    }
    return render(request, 'pages/layout-fluid-vertical.html', context)

def changelog(request):
    return render(request, 'pages/changelog.html')

def profile(request):
    return render(request, 'pages/profile.html')

def icons(request):
    context = {
        'parent': '',
        'segment': 'icons',
    }
    return render(request, 'pages/icons.html', context)

def finance_tracker_settings(request):

    if request.method == 'GET': # When load the URL first time

        platformCategory = PlatformCategory.objects.all() # Fetch all Platform objects
        incomeCategory = IncomeCategory.objects.all() # Fetch all Platform objects
        expenseCategory = ExpenseCategory.objects.all() # Fetch all Platform objects
        savingCategory = SavingCategory.objects.all() # Fetch all Platform objects
        debugCategory = DebugCategory.objects.all() # Fetch all Platform objects

        context = {
            'parent': '',
            'segment': 'finance_tracker_settings',
            'platformCategory': platformCategory,
            'incomeCategory': incomeCategory,
            'expenseCategory': expenseCategory,
            'savingCategory': savingCategory,
            'debugCategory': debugCategory
        }
        return render(request, 'pages/expense_tracking/settings.html', context)
    
    else:
        if request.POST.get('action', None) == 'add_new_item':
            newName = request.POST.get('newName', None)
            newDescription = request.POST.get('newDescription', None)
            newEnabled = request.POST.get('newEnabled', None)

            print(newName)

            selectedModel = request.POST.get('selectedModel', None)
            match selectedModel:
                case 'PlatformCategory':
                    model = PlatformCategory
                case 'IncomeCategory':
                    model = IncomeCategory
                case 'ExpenseCategory':
                    model = ExpenseCategory
                case 'SavingCategory':
                    model = SavingCategory   
                case 'DebugCategory':
                    model = DebugCategory

            record = model.objects.create(
                name=newName,
                description=newDescription,
                enabled=newEnabled,
                user=request.user,
            )
            try:
                record.save()
                print('Saved new item')

            except IntegrityError as e:
                print(f'Error: {e}')  # Print the specific IntegrityError for debugging
                return JsonResponse({'Error': 'Cannot pass new object(s) to the model'}, status=400)

            # Serialize the record data before returning it in JsonResponse
            serialized_data = {
                'id': record.id,
                'name': record.name,
                'description': record.description,
                'enabled': record.enabled,
            }
            return JsonResponse({'data': serialized_data}, status=200)
        
        else: # action = 'update_item'
            updateValue = request.POST.get('updateValue', None)
            cell_id = request.POST.get('cell_id', None)
            cell_column = request.POST.get('cell_column', None)

            selectedModel = request.POST.get('selectedModel', None)
            print(selectedModel)

            match selectedModel:
                case 'PlatformCategory':
                    model = PlatformCategory
                case 'IncomeCategory':
                    model = IncomeCategory
                case 'ExpenseCategory':
                    model = ExpenseCategory
                case 'SavingCategory':
                    model = SavingCategory 
                case 'DebugCategory':
                    model = DebugCategory 

            record = model.objects.get(id=int(cell_id))
            
            match cell_column:
                case 'name':
                    record.name = updateValue
                case 'description':
                    record.description = updateValue
                case 'enabled':
                    record.enabled = updateValue

            record.user = request.user

            try:
                record.save()
                print('Saved updateValue')
                # Serialize the record data before returning it in JsonResponse
                serialized_data = {
                    'id': record.id,
                    'name': record.name,
                    'description': record.description,
                    'enabled': record.enabled,
                }
                return JsonResponse({'data': serialized_data})

            except IntegrityError as e:
                print(f'Error: {e}')  # Print the specific IntegrityError for debugging
                return JsonResponse({'Error': 'Cannot pass new object(s) to the model'}, status=400)
    

def summary_income_expense(request):
    context = {
        'parent': 'summary',
        'segment': 'summary_income_expense',
    }
    return render(request, 'pages/expense_tracking/summary_income_expense.html', context)

def summary_asset(request):
    context = {
        'parent': 'summary',
        'segment': 'summary_asset',
    }
    return render(request, 'pages/expense_tracking/summary_asset.html', context)

def data_goal_budget(request):
    context = {
        'parent': 'data_table',
        'segment': 'data_goal_budget',
    }
    return render(request, 'pages/expense_tracking/data_goal_budget.html', context)

def data_income_expense(request):
    
    if request.method == 'GET': # When load the URL first time
        incomeExpenseData = IncomeExpenseData.objects.all() # Fetch all Platform objects

        # Access the currency choices from the model
        currencyChoices = IncomeExpenseData.currencyChoices
        platformCategoryChoices = PlatformCategory.objects.all().values('id', 'name', 'enabled')
        incomeCategoryChoices = IncomeCategory.objects.all().values('id', 'name', 'enabled')
        expenseCategoryChoices = ExpenseCategory.objects.all().values('id', 'name', 'enabled')
        savingCategoryChoices = SavingCategory.objects.all().values('id', 'name', 'enabled')

        #test = IncomeExpenseData.objects.get(id=1).transactionDateTime
        #print(test)

        context = {
            'parent': '',
            'segment': 'data_income_expense',
            'incomeExpenseData': incomeExpenseData,
            'currencyChoices': list(currencyChoices),  # Convert QuerySet to list of dicts
            'platformCategoryChoices': list(platformCategoryChoices),  # Convert QuerySet to list of dicts
            'incomeCategoryChoices': list(incomeCategoryChoices), # Convert QuerySet to list of dicts
            'expenseCategoryChoices': list(expenseCategoryChoices), # Convert QuerySet to list of dicts
            'savingCategoryChoices': list(savingCategoryChoices), # Convert QuerySet to list of dicts
            'UserIsAuthenticated': request.user.is_authenticated
        }
        return render(request, 'pages/expense_tracking/data_income_expense.html', context)
    
    else: #request.method = post

        if not request.user.is_authenticated:
            return redirect('login')

        updateValue = request.POST.get('updateValue', None)
        dataType = request.POST.get('dataType', None)
        bSubList = request.POST.get('bSubList', None) 
        cell_id = request.POST.get('cell_id', None)
        cell_column = request.POST.get('cell_column', None)

        
        record = IncomeExpenseData.objects.get(id=int(cell_id))

        """     # Get updateObject if dataType is 'list'
        if 'list' == dataType:
            if 'true' == bSubList:
                updateObject = PlatformCategory.objects.get(id=int(updateValue)) #still need to fix this. it needs to be different as it's not a modal.
            else:
                updateObject = PlatformCategory.objects.get(id=int(updateValue))

        # Create a mapping for cell_column to record attributes
        column_model_list_mapping = {
            'transactionDateTime': None,
            'platform': PlatformCategory,
            'category': updateObject,
            'rawAmount': updateValue,
            'rawCurrency': updateObject,
            'note': updateValue
        } """

        # Create a mapping for cell_column to record attributes
        column_attributes_mapping = {
            'transactionDateTime': updateValue,
            'platform': updateValue,
            'category': updateValue,
            'rawAmount': updateValue,
            'rawCurrency': updateValue,
            'note': updateValue
        }

        # Update the record if cell_column is valid
        if cell_column in column_attributes_mapping:
            setattr(record, cell_column, column_attributes_mapping[cell_column])
        else:
            print("cell_column not found")
            
        record.lastEdit = datetime.datetime.now()
        record.lastEditBy = request.user
            

        try:
            record.save()
            print('Saved updateValue')
            # Serialize the record data before returning it in JsonResponse
            serialized_data = {
                'transactionDateTime': record.transactionDateTime,
                'category': record.category,
                'rawAmount': record.rawAmount,
                'rawCurrency': record.rawCurrency,
                'note': record.note,
                'lastEdit': record.lastEdit,
                'lastEditBy': record.lastEditBy.username,
            }
            return JsonResponse({'data': serialized_data})

        except IntegrityError as e:
            print(f'Error: {e}')  # Print the specific IntegrityError for debugging
            return JsonResponse({'Error': 'Cannot pass new object(s) to the model'}, status=400)



def data_asset(request):
    context = {
        'parent': 'data_table',
        'segment': 'data_asset',
    }
    return render(request, 'pages/expense_tracking/data_asset.html', context)

def add_income_expense(request):

    platformCategory = PlatformCategory.objects.all()
    incomeCategory = IncomeCategory.objects.all() # Fetch all Platform objects
    expenseCategory = ExpenseCategory.objects.all() # Fetch all Platform objects
    incomeExpenseData = IncomeExpenseData.objects.all()# Fetch all Platform objects

    if request.method == 'GET': # When load the URL first time

        """         if not request.user.is_authenticated:
        return redirect('login')  """

        # Access the currency choices from the model
        currencyChoices = IncomeExpenseData.currencyChoices

        context = {
            'parent': '',
            'segment': 'data_income_expense',
            'platformCategory': platformCategory,
            'incomeCategory': incomeCategory,
            'expenseCategory': expenseCategory,
            'incomeExpenseData': incomeExpenseData,
            'currencyChoices': currencyChoices,  # Pass the currency choices to the context
        }
        return render(request, 'pages/expense_tracking/add_income_expense.html', context)
    
    else:
            print('at view.py')
            addTransactionDateTime = request.POST.get('transactionDateTime', None)
            addPlatform = request.POST.get('platform', None)
            addCategory = request.POST.get('category', None)
            addRawAmount = request.POST.get('rawAmount', None)
            addRawCurrency = request.POST.get('rawCurrency', None)
            addNote = request.POST.get('note', None)
            addCategoryType = request.POST.get('categoryType', None)
            print(addPlatform)

            #matchedPlatform = PlatformCategory.objects.filter(name=addPlatform).first()

            record = IncomeExpenseData.objects.create(
                transactionDateTime = addTransactionDateTime,
                platform = addPlatform,
                category = addCategory,
                categoryType = addCategoryType,
                rawAmount = addRawAmount,
                rawCurrency = addRawCurrency,
                note = addNote,
                lastEdit = datetime.datetime.now(),
                lastEditBy = request.user
            )
            try:
                record.save()

            except IntegrityError as e:
                print(f'Error: {e}')  # Print the specific IntegrityError for debugging
                return JsonResponse({'Error': 'Cannot add new item'}, status=400)

            serialized_data = {
                'transactionDateTime': record.transactionDateTime,
                'platform': record.platform,
                'category': record.category,
                'rawAmount': record.rawAmount,
                'rawCurrency': record.rawCurrency,
                'note': record.note
            }
            return JsonResponse({'data': serialized_data}, status=200)

def add_saving(request):

   #if request.method == 'GET': # When load the URL first time
    platformCategory = PlatformCategory.objects.all()
    savingCategory = SavingCategory.objects.all() # Fetch all Platform objects
    incomeExpenseData = IncomeExpenseData.objects.all() # Fetch all Platform objects

    # Access the currency choices from the model
    currencyChoices = IncomeExpenseData.currencyChoices

    context = {
        'parent': 'add',
        'segment': 'add_saving',
        'platformCategory': platformCategory,
        'savingCategory': savingCategory,
        'incomeExpenseData': incomeExpenseData,
        'currencyChoices': currencyChoices,  # Pass the currency choices to the context
    }

    return render(request, 'pages/expense_tracking/add_saving.html', context)
