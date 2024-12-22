from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from .models import Job
from .serializers import JobSerializer

def api_home(request):
    """
    Default view for the /api/ endpoint.
    """
    return JsonResponse({"message": "Welcome to the Job Listing API!"})

@api_view(['GET'])
def get_jobs(request):
    """
    Retrieve all job listings.
    Optionally, filter jobs by title or company_name using query parameters.
    Example: /api/jobs/?title=Engineer&company_name=Google
    """
    title = request.GET.get('title')
    company_name = request.GET.get('company_name')

    jobs = Job.objects.all()

    # Filter by title if the parameter is provided
    if title:
        jobs = jobs.filter(title__icontains=title)
    
    # Filter by company_name if the parameter is provided
    if company_name:
        jobs = jobs.filter(company_name__icontains=company_name)

    # Check if any jobs were found
    if not jobs.exists():
        return Response({"message": "No jobs found matching the criteria."}, status=status.HTTP_200_OK)

    serializer = JobSerializer(jobs, many=True)
    return Response({"jobs": serializer.data}, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_job(request):
    """
    Create a new job listing.
    """
    serializer = JobSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "Job created successfully", "job": serializer.data},
            status=status.HTTP_201_CREATED
        )
    return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_job_detail(request, pk):
    """
    Retrieve a specific job listing by its ID.
    """
    try:
        job = Job.objects.get(pk=pk)
        serializer = JobSerializer(job)
        return Response({"job": serializer.data}, status=status.HTTP_200_OK)
    except Job.DoesNotExist:
        return Response(
            {"error": f"Job with ID {pk} not found"},
            status=status.HTTP_404_NOT_FOUND
        )
