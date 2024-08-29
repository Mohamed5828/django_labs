import pandas as pd
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import json
import os

# Path to your Excel file
EXCEL_FILE_PATH = 'orders.xlsx'

def read_excel_file():
    if not os.path.exists(EXCEL_FILE_PATH):
        return []

    try:
        df = pd.read_excel(EXCEL_FILE_PATH, engine='openpyxl')
        return df.to_dict(orient='records')
    except Exception as e:
        raise RuntimeError(f"Error reading Excel file: {str(e)}")

def write_to_excel(data):
    headers = ['orderID', 'orderName', 'userName', 'status']
    
    try:
        if os.path.exists(EXCEL_FILE_PATH):
            df = pd.read_excel(EXCEL_FILE_PATH, engine='openpyxl')
        else:
            df = pd.DataFrame(columns=headers)
        
        new_data_df = pd.DataFrame(data, columns=headers)
        df = pd.concat([df, new_data_df], ignore_index=True)

        df.to_excel(EXCEL_FILE_PATH, index=False, engine='openpyxl')
    except Exception as e:
        raise RuntimeError(f"Error writing to Excel file: {str(e)}")

@csrf_exempt
def order_view(request):
    if request.method == 'GET':
        try:
            data = read_excel_file()
            return render(request, 'home.html', {'data': data})
        except RuntimeError as e:
            return HttpResponseBadRequest(str(e))
        
    elif request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))

            if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
                return HttpResponseBadRequest("Invalid JSON format. Expected a list of dictionaries.")

            write_to_excel(data)
            return JsonResponse({'message': 'Excel file updated successfully'})

        except json.JSONDecodeError:
            return HttpResponseBadRequest("Invalid JSON data")
        except ValueError as e:
            return HttpResponseBadRequest(str(e))
        except Exception as e:
            return HttpResponseBadRequest(f"Error processing request: {str(e)}")
