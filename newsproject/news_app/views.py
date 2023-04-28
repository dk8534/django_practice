from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request,'home.html')


def aligarh_view(request):
    city = 'Aligarh'
    head_msg = 'Aligarh City Breaking News'
    n1 = 'Aligarh News: तीन फीट के दूल्हा-दुल्हन, वेलेंटाइन डे पर शहर में हुआ अनोखा निकाह'
    n2 = 'Aligarh Exhibition: नुमाइश में सुनामी झूले का लॉक टूटा, गिरकर छह दर्शक हुए घायल'
    n3 = 'Aligarh News: 25 फरवरी से 6 दिन तक बंद रहेंगे बिजली संबंधी आनलाइन काम, पहले ही जमा कर लें बिल'
    n4 = 'Aligarh Mahotsav: अलीगढ़ की नुमाइश में सिंगर हर्षित सक्सेना नाइट, आज के ये हैं प्रोग्राम'
    n5 = 'मलखान सिंह हत्याकांड: सोनू गौतम की फरारी का सहयोगी मुठभेड़ में जख्मी, गिरफ्तार कर भेजा जेल'
    type = 'aligarh'
    context={'n1':n1,'n2':n2,'n3':n3,'n4':n4,'n5':n5,'head_msg':head_msg,'city':city,'type':type}
    return render(request,'news.html',context)

def noida_view(request):
    city = 'Noida'
    head_msg = 'Noida City Breaking News'
    n1 = 'नोएडा: यमुना प्राधिकरण क्षेत्र के हजारों किसानों का मिलेगा 778 रुपये प्रति वर्गमीटर बढ़ा मुआवजे का लाभ'
    n2 = 'नोएडा: विदेशी टूर व सेमिनार के नाम पर 100 डॉक्टरों से ठगी करने वाला गया जेल'
    n3 = 'Greater Noida: वाहन चोर गिरोह का पर्दाफाश, तीन आरोपी गिरफ्तार; 10 बाइक और एक स्कूटी बरामद'
    n4 = 'Noida: विदेशी टूर और सेमिनार के नाम पर 100 डॉक्टरों से ठगी करने वाला गया जेल, पश्चिम बंगाल से किया था गिरफ्तार'
    n5 = 'नोएडा: भाजपा नेता ने व्हाट्सएप ग्रुप पर डाले राजनीतिक वीडियो, एडमिन ने ग्रुप से निकाला तो कर दी एफआईआर'
    type = 'noida'
    context={'n1':n1,'n2':n2,'n3':n3,'n4':n4,'n5':n5,'head_msg':head_msg,'city':city,'type':type}
    return render(request,'news.html',context)

def delhi_view(request):
    city = 'Delhi'
    head_msg = 'Delhi City Breaking News'
    n1 = 'Nikki Murder Case: गोवा भागने का प्लान... फिर साथ में आत्महत्या का इरादा, लेकिन ऐसे बिगड़ा खेल'
    n2 = 'Delhi Murder Case: कोचिंग सेंटर में प्यार... फिर लिव इन में रहे साहिल और निक्की, अब फ्रिज में मिली लाश'
    n3 = 'Nikki Murder Case: शव को ठिकाने लगाने और पुलिस को चकमा देने की ये थी साजिश, साहिल का खुलासा कर देगा हैरान'
    n4 = 'चमत्कार है ये!: 15 मिनट तक साबुन के पानी से भरे वॉशिंग मशीन में गिरकर पड़ा रहा मासूम, डॉक्टरों ने ऐसे बचाया'
    n5 = 'Valentine Day: पार्क में बैठे थे दंपती, संगठन ने पत्नी के सामने पति को पीटा; प्रेमी जोड़ा समझ लगाई मार'
    type = 'delhi'
    context={'n1':n1,'n2':n2,'n3':n3,'n4':n4,'n5':n5,'head_msg':head_msg,'city':city,'type':type}
    return render(request,'news.html',context)