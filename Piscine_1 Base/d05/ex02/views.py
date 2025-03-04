from django.shortcuts import render
from .forms import LogForm
import os
from django.conf import settings
from datetime import datetime

# Create your views here.
def log(request):
    log_file = settings.LOG_FILE_PATH

    history = []
    if os.path.exists(log_file):
        with open(log_file, 'r') as file:
            history = file.readlines()
    
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            entry = f'{timestamp} - {text}\n'

            # Append the new entry to the log file
            with open(log_file, 'a') as file:
                file.write(entry)
            
            history.append(entry)
    
    else:
        form = LogForm()
    
    return render(request, 'log.html', {'form': form, 'history': history})
