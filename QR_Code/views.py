from django.shortcuts import render
import qrcode


def create_qr(request):
        
    link = request.GET.get('link')  

    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4,)
    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save('static/qr_images/code.png')  
    return render(request=request, template_name='hi.html', context={'qr_image': 'qr_code.png'})