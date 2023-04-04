# from django.shortcuts import render, redirect
# from .models import Plant, Tool, Tag
# from .forms import PlantForm, TagForm, ToolForm
#
# # Create your views here.
# def mainPage(request):
#     return render(request, 'main.html')
#
# # Plant
# def plantPage(request):
#     plants = Plant.objects.all()
#     context = {'plants':plants}
#     return render(request, 'Backend/plantsTable.html', context)
#
# def createPlant(request):
#     form = PlantForm()
#
#     if request.method == 'POST':
#         form = PlantForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('plants')
#
#     context = {'form': form}
#     return render(request, 'Backend/plantForm.html', context)
#
# def updatePlant(request, pk):
#     plantObj = Plant.objects.get(id=pk)
#     form = PlantForm(instance=plantObj)
#     print(plantObj.id)
#     if request.method == 'POST':
#         form = PlantForm(request.POST, request.FILES, instance=plantObj)
#         if form.is_valid():
#             form.save()
#             return redirect('plants')
#
#     context = {'form': form}
#     return render(request, 'Backend/plantForm.html', context)
#
#
# def deletePlant(request, pk):
#     plantObj = Plant.objects.get(id=pk)
#
#     if request.method == 'POST':
#         plantObj.delete()
#         return redirect('plants')
#
#     context = {'plant': plantObj}
#     return render(request, 'Backend/plantDelete.html', context)
#
# # Tool
# def toolPage(request):
#     tools = Tool.objects.all()
#     context = {'tools':tools}
#     return render(request, 'Backend/toolsTable.html', context)
#
# def createTool(request):
#     form = ToolForm()
#
#     if request.method == 'POST':
#         form = ToolForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('tools')
#
#     context = {'form': form}
#     return render(request, 'Backend/toolForm.html', context)
#
# def updateTool(request, pk):
#     toolObj = Tool.objects.get(id=pk)
#     form = ToolForm(instance=toolObj)
#
#     if request.method == 'POST':
#         form = ToolForm(request.POST, request.FILES, instance=toolObj)
#         if form.is_valid():
#             form.save()
#             return redirect('tools')
#
#     context = {'form': form}
#     return render(request, 'Backend/toolForm.html', context)
#
#
# def deleteTool(request, pk):
#     toolObj = Tool.objects.get(id=pk)
#
#     if request.method == 'POST':
#         toolObj.delete()
#         return redirect('tools')
#
#     context = {'tool': toolObj}
#     return render(request, 'Backend/toolDelete.html', context)
#
# # Tag
# def tagPage(request):
#     tags = Tag.objects.all()
#     context = {'tags':tags}
#     return render(request, 'Backend/tagsTable.html', context)
#
# def createTag(request):
#     form = TagForm()
#
#     if request.method == 'POST':
#         form = TagForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('tags')
#
#     context = {'form': form}
#     return render(request, 'Backend/tagForm.html', context)
#
# def updateTag(request, pk):
#     tagObj = Tag.objects.get(id=pk)
#     form = TagForm(instance=tagObj)
#
#     if request.method == 'POST':
#         form = TagForm(request.POST, request.FILES, instance=tagObj)
#         if form.is_valid():
#             form.save()
#             return redirect('tags')
#
#     context = {'form': form}
#     return render(request, 'Backend/tagForm.html', context)
#
#
# def deleteTag(request, pk):
#     tagObj = Tag.objects.get(id=pk)
#
#     if request.method == 'POST':
#         tagObj.delete()
#         return redirect('tags')
#
#     context = {'tag': tagObj}
#     return render(request, 'Backend/tagDelete.html', context)
