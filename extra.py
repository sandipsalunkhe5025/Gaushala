# #view.py
# @api_view(['GET'])
# def filter_and_download_report(request):
#     if request.method == 'GET':
#         division = request.GET.get('division')
#         district = request.GET.get('district')
#         gaushala = request.GET.get('gaushala')
#         gaushala_no = request.GET.get('gaushala_no')
#         date_from = request.GET.get('date_from')
#         date_to = request.GET.get('date_to')
#         filtered_data = cattleData.objects.all()
#         if division:
#             filtered_data = filtered_data.filter(division=division)
#         if district:
#             filtered_data = filtered_data.filter(district=district)
#         if gaushala:
#             filtered_data = filtered_data.filter(gaushala=gaushala)
#         if gaushala_no:
#             filtered_data = filtered_data.filter(gaushala_no=gaushala_no)
#         if date_from and date_to:
#             filtered_data = filtered_data.filter(date__range=(date_from, date_to))
#
#         data_list = list(filtered_data.values())
#         df = pd.DataFrame(data_list)
#         csv_report = df.to_csv(index=False)
#         response = HttpResponse(csv_report, content_type='text/csv')
#         response['Content-Disposition'] = 'attachment; filename="cattle_data_report.csv"'
#         return response
#
# #urls.py
#  path('filter-and-download-report/', views.filter_and_download_report, name='filter_and_download_report'),
#
# #Cattle_management_overview.html
# <!-- Assume this is your search menu bar -->
# <form action="{% url 'filter_and_download_report' %}" method="get">
#     <label for="division">Division:</label>
#     <input type="text" id="division" name="division">
#     <!-- Add other search criteria inputs here -->
#
#     <!-- Add a submit button to trigger the search -->
#     <button type="submit">Search</button>
# </form>
#
# <!-- Add a download button -->
# <a href="{% url 'filter_and_download_report' %}?{{ request.GET.urlencode }}&download=true" class="btn btn-primary">Download Report</a>
