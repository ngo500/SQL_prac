from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from .models import Course, Lesson, Enrollment
from django.urls import reverse
from django.views import generic, View
from django.http import Http404

# from base View class, subclass CourseListView
class CourseListView(View):
    
    # Handles GET request
    def get(self, request):
        context = {}

        # Query top 10 popular courses based off total_enrollment
        course_list = Course.objects.order_by('-total_enrollment')[:10]

        # Append list to context
        context['course_list'] = course_list

        # Render page using course_list template and context
        return render(request, 'onlinecourse/course_list.html', context)

# from base View class, subclass EnrollView
class EnrollView(View):

    # Handles POST request
    def post(self, request, *args, **kwargs):
        # Get course_id of class being enrolled into
        course_id = kwargs.get('pk')
        # Get object of course or 404
        course = get_object_or_404(Course, pk=course_id)
        # Increase total enrollment by 1
        course.total_enrollment += 1
        course.save()
        # Redirect course details page
        return HttpResponseRedirect(reverse(viewname='onlinecourse:course_details', args=(course.id,)))

# from base View class, subclass CourseDetailsView
class CourseDetailsView(View):

    # Handles GET request
    def get(self, request, *args, **kwargs):
        context = {}
        # Get course_id from URL
        course_id = kwargs.get('pk')
        try:
            # Get the course object based on course_id
            course = Course.objects.get(pk=course_id)
            # Append the course object to context
            context['course'] = course
            # Render page using template and course_id
            return render(request, 'onlinecourse/course_detail.html', context)
        except Course.DoesNotExist:
            raise Http404("No course found matching the given id.")
