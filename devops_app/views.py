from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Reporter
from .serializers import ReporterSerializer


class ReporterListCreateView(APIView):
    def get(self, request):
        reporters = Reporter.objects.all()
        serializer = ReporterSerializer(reporters, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReporterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReporterRetrieveUpdateDestroyView(APIView):
    def get_object(self, pk):
        try:
            return Reporter.objects.get(pk=pk)
        except Reporter.DoesNotExist:
            return None

    def get(self, request, pk):
        reporter = self.get_object(pk)
        if reporter is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ReporterSerializer(reporter)
        return Response(serializer.data)

    def put(self, request, pk):
        reporter = self.get_object(pk)
        if reporter is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ReporterSerializer(reporter, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        reporter = self.get_object(pk)
        if reporter is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        reporter.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
