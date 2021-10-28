from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.serializers import Serializer
from .serializers import TodolistSerializer
from .models import Todolist

# Get Data
@api_view(['GET'])
def all_todolist(request):
    alltodolist = Todolist.objects.all()
    serializer = TodolistSerializer(alltodolist, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

#Post data
@api_view(['POST'])
def post_todolist(request):
    if request.method == 'POST':
        serializer = TodolistSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

#Edit data
@api_view(['PUT'])
def update_todolist(request, TID):
    if request.method == 'PUT':
        todo = Todolist.objects.get(id=TID)
        data = {}
        serializer = TodolistSerializer(todo,data=request.data)
        if serializer.is_valid() :
            serializer.save()
            data['status'] = 'updated'
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

#Delete data
@api_view(['DELETE'])
def delete_todolist(request, TID):
    if request.method == 'DELETE':
        todo = Todolist.objects.get(id=TID)
        data = {}
        delete = todo.delete()
        if delete:
            data['status'] = 'deleted'
            statuscode = status.HTTP_200_OK
        else:
            data['status'] = 'failed'
            statuscode = status.HTTP_400_BAD_REQUEST
        return Response(data=data, status=statuscode)




data = [
    {
        "title": "วัคซีนโควิดคืออะไร? 1234",
        "subtitle": "วัคซีนโควิด คือ วัคซีนที่ใช้สำหรับการป้องกันไวรัสโควิด 19",
        "imageurl": "https://raw.githubusercontent.com/zent-bank/FlutterAPI/main/assets/images/vaccine-5926664_960_720.jpg",
        "detail" : "วัคซีนป้องกันโรคติดเชื้อไวรัสโคโรนา 2019 (COVID-19) ซึ่งในขณะนี้มีด้วยกัน 4 ชนิดหลักๆ แบ่งตามเทคนิคที่ใช้ในการผลิตวัคซีน คือ\n\rmRNA vaccines เป็นการผลิตโดยใช้สารพันธุกรรมของเชื้อไวรัสซาร์ส-โควี-2 (SARS-CoV-2) เมื่อฉีดเข้าไปในร่างกาย จะทำให้ร่างกายสร้างโปรตีนที่สามารถกระตุ้นการสร้างภูมิคุ้มกันต่อเชื้อไวรัสขึ้นมา\n\rViral vector vaccines เป็นการฝากสารพันธุกรรมของเชื้อไวรัสซาร์ส-โควี-2 (SARS-CoV-2) เข้าไปในสารพันธุกรรมของไวรัสชนิดอื่นที่อยู่ในสภาพที่ไม่ก่อให้เกิดโรค เพื่อพาเข้ามาในร่างกาย ทำให้ร่างกายสร้างภูมิคุ้มกันต่อเชื้อไวรัสขึ้นมา\n\rProtein-based vaccines จะใช้โปรตีนบางส่วนของเชื้อไวรัสซาร์ส-โควี-2 (SARS-CoV-2) เช่น โปรตีนส่วนหนาม (spike protein) ฉีดเข้าไปในร่างกายเพื่อกระตุ้นให้ร่างกายสร้างภูมิคุ้มกันต่อเชื้อไวรัส\n\rInactivated vaccines ผลิตโดยการใช้ไวรัสซาร์ส-โควี-2 (SARS-CoV-2) ที่ถูกทำให้ตายแล้ว เมื่อฉีดเข้าไปในร่างกาย จะกระตุ้นให้ร่างกายสร้างภูมิคุ้มกันต่อเชื้อไวรัส"
    },
    {
        "title": "ควรฉีดวัคซีนหรือไม่?",
        "subtitle": "ควรฉีด เนื่องจากจะป้องกันการป่วยหนักได้",
        "imageurl": "https://raw.githubusercontent.com/zent-bank/FlutterAPI/main/assets/images/keys-5170080_960_720.jpg",
        "detail" : "การฉีดวัคซีนป้องกันโรคโควิด-19 สามารถลดความรุนแรงของอาการป่วยและลดการเสียชีวิตได้ เนื่องจากสถานการณ์การระบาดของโรคโควิด-19 ถือเป็นภาวะฉุกเฉินของโลก จำนวนผู้ติดเชื้อไวรัสโคโรนา 2019 (COVID-19) ทั่วโลกกว่าร้อยล้านคน มีผู้เสียชีวิตมากกว่าสองล้านคน โดยในปัจจุบันมีการฉีดวัคซีนรวมทั่วโลกแล้วกว่า 100 ล้านโดส สำหรับประเทศที่มีการฉีดวัคซีนป้องกัน COVID-19 มากที่สุด คือ สหรัฐอเมริกา รองลงมาคือ ประเทศจีน และอังกฤษตามลำดับ (ข้อมูลวันที่ 9 ก.พ. 2564)"
    },
    {
        "title": "ฉีดวัคซีนที่ไหน?",
        "subtitle": "สามารถฉีดได้จากสถานที่ ที่รัฐฯ เปิดให้ฉีดได้เลย",
        "imageurl": "https://raw.githubusercontent.com/zent-bank/FlutterAPI/main/assets/images/medic-563425_960_720.jpg",
        "detail" : "1.พื้นที่กรุงเทพฯ ให้ใช้ระบบของกรุงเทพมหานคร หรือระบบอื่นที่เปิดบริการ เช่น \n\r27 พฤษภาคม 2564 ตั้งแต่ 12.00 น. เปิดลงทะเบียนวัคซีนโควิดฟรีโครงการไทยร่วมใจ \"กรุงเทพฯ ปลอดภัย\" ให้ผู้ที่อาศัยอยู่ในกรุงเทพฯ อายุตั้งแต่ 18-59 ปี ที่ไม่ได้เป็น 7 กลุ่มโรคเสี่ยงผ่านเว็บไซต์ www.ไทยร่วมใจ.com\n\r2.ต่างจังหวัด ทั้ง 76 จังหวัด ดำเนินการผ่านช่องทางต่อไปนี้        \n\rอาสาสมัครสาธารณสุขประจำหมู่บ้าน (อสม.) / โรงพยาบาลส่งเสริมสุขภาพตำบล (รพ.สต.)/ โรงพยาบาลรัฐใกล้บ้าน (ไม่จำเป็นต้องมีประวัติ)\n\rระบบออนไลน์ (แอปพลิเคชัน/ เว็บไซต์ หรือแพลตฟอร์มอื่นๆ) ของแต่ละจังหวัด\n\rหมอพร้อม LINE OA/ แอปผลิเคชันหมอพร้อม เมื่อเปิดให้บริการอีกครั้ง สามารถกดได้ที่ลิ้งก์ line://ti/p/@475ptmfj หรือแอดไลน์ \"หมอพร้อม\\” ทั้งนี้ระบบหมอพร้อมยังใช้งานได้ตามปกติสำหรับประชาชนทุกกลุ่ม ในการแสดงข้อมูลหลังการฉีดวัคซีน แจ้งนัดหมายในการฉีดเข็มที่ 2 และการเป็นหลักฐานประกอบการขอใบรับรองการฉีดวัคซีนโควิด\n\rสอบถามเพิ่มเติม Call Center : 02 792 2333"
    },
    {
        "title": "ประวัติการฉีดวัคซีน",
        "subtitle": "ฉีดวัคซีนกี่ครั้งแล้ว",
        "imageurl": "https://raw.githubusercontent.com/zent-bank/FlutterAPI/main/assets/images/covid-19-6553695_960_720.jpg",
        "detail" : "ฉีดแล้วจ้าาาา ครั้งเดียว!!!"
    }
]

def Home(request):
    return JsonResponse(data=data, safe=False, json_dumps_params={'ensure_ascii':False})