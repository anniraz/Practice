from rest_framework import viewsets,status
from rest_framework.response import Response

from apps.product.models import Product
from apps.product.serializers import ProductSerializer
# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):

    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        user=request.user
        product=Product.objects.filter(user=user)
        if len(product)>25:
            return Response({'error':"you can't add products more then 25"})
        else:
            serializer=self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        # return super().create(request, *args, **kwargs)




    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # context['comments'] = Comment.objects.filter(item=self.object)
    #     # context['form'] = CommentCreationForm()
    #     num_visits = self.request.session.get('num_visits', 0)
    #     self.request.session['num_visits'] = num_visits + 1
    #     context['visits'] = num_visits
    #     return context
