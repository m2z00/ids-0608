from django.views.generic.base import View
from django.shortcuts import render
from .models import DjangoBoard,UserInfo


class login(View):
    def get(self, request):
        return render(request, 'pie/login.html')

    def post(self, request):
        id = request.POST.get('userid')
        pw = request.POST.get('userpw')
        msg = False
        infos = UserInfo.objects.all()
        for info in infos:
            if info.userid == id and info.userpw == pw:
                name = info.username
                msg = True
        context = {
            'msg': msg,
        }

        #그래프 변수 설정 (파이그래프 1,2) , (라인그래프 1,2)
        # protocol
        labels = []
        data = []

        #pps
        labels2 = []
        data2 = []

        #src ip
        labels3 = []
        data3 = []

        #flow-duration
        labels4 = []
        data4 = []

        #src port
        labels5 = []
        data5 = []
        # top 5의 프로토콜 선별해서 queryset에 넣기

        #protocol
        top_five = DjangoBoard.objects.values('protocol').filter(label=1).distinct()[:5]
        #src_ip
        top_five_ = DjangoBoard.objects.values('srcip').filter(label=1).distinct()[:5]
        #src_port
        top_five__ = DjangoBoard.objects.values('srcport').filter(label=1).distinct()[:5]

        #labels_ddos

        labels_ddos = DjangoBoard.objects.filter(label=1)
        #pps&flow-duration
        pps = DjangoBoard.objects.order_by('id')
        #공격 카운트
        attack_count = DjangoBoard.objects.filter(label=1).count()
        #로그 출력
        logg = DjangoBoard.objects.order_by('id')
        # top 5의 프로토콜 for문으로 돌려가며 filter 처리후 count 세기



        #protocol 파이 그래프
        for city in top_five:
            labels.append(city['protocol'])
            data.append(labels_ddos.filter(protocol=city['protocol']).count())

        #src 파이 그래프
        for src in top_five_:
            labels3.append(src['srcip'])
            data3.append(labels_ddos.filter(srcip=src['srcip']).count())
        #src port 파이 그래프
        for src in top_five__:
            labels5.append(src['srcport'])
            data5.append(labels_ddos.filter(srcport=src['srcport']).count())
        #pps, duration 라인그래프
        for a in pps:
            labels2.append(a.id)
            labels4.append(a.id)
            data2.append(a.flowpackets_s)
            data4.append(a.flowduration)


        #변수 랜더링
        return render(request, 'pie/pie_chart.html', {
            'labels': labels,
            'data': data,
            'labels2': labels2,
            'data2': data2,
            'labels3': labels3,
            'data3': data3,
            'labels4': labels4,
            'data4': data4,
            'labels5': labels5,
            'data5': data5,
            'attack_count': attack_count,
            'logg': logg
        })
