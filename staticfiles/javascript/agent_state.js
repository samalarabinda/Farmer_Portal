document.addEventListener('DOMContentLoaded', function () {
        const districtInput = document.getElementById("districtInput");
        const districtList = document.getElementById("districtList");
        const districts = ["Cuttack Sadar","Baranga","Kantapada","Niali","Tangi-Chowdwar","Salipur","Nischintakoili","Mahanga"," Athgarh","Tigiria",
        "Baramba","Narasinghpur","Banki","Dampara","Jajpur","Binjharpur","Korei","Bari","Rasulpur","Dasarathpur"," Sukinda","Dangadi","Dharmasala",
        "Badachana","Jagatsinghpur","Raghunathpur","Biridi-F","Balikuda","Nuagaon","Tirtol"," Kujang","Erasma","Kendrapara","Derabis","Marsaghai",
        "Mahakalapada","Garadpur","Pattamundai","Rajnagar"," Aul","Rajkanika","Balasore","Remuna","Basta"," Baliapal","Bhograi","Jaleswar","Bahanaga",
        "Soro","Simulia","Khaira","Nilgiri","Oupada","Bhadrak","Bonth","Basudevpur","Tihidi","Chandabali"," Dhamnagar","Bhandaripokhari","Krushna- prasad",
        "Brahmagiri"," Sadar"," Gop","Kakatpur","Astarang","Nimapara","Pipili","Delang","Kanas","Satyabadi","Bhubaneswar","Jatni","Balipatna","Balianta",
        "Khurda","Tangi","Banpur","Bolgarh","Chilika","Begunia","Nayagarh","Ranpur","Odagaon","Nuagaon","Khandapada"," Bhapur","Daspalla","Gania",
        "Rairangpur","Bijatala","Bisoi","Jamda","Bahalda","Tiring","Kusumi","Baripada","Kuliana","Suliapada","Rasgovindpur","Morada","Samakhunta",
        "Bodasahi","Bangiriposi","Betnati","Sarasakana","Udala","Kaptipada","Khunta","Gopabandhunagar"," Karanjia","Thakurmunda"," Jasipur","Sukruli",
        "Raruan","Sadar"," Odapada","Gondia","Hindol","Kamakhyanagar","Kankadahad"," Bhuban"," Parjang","Anugul","Banarpal","Chhendipada","Talcher",
        " Kaniha","Athmallik","Kishorenagar","Pallahara","Bolangir","Loisinga","Puintala","Agalpur"," Deogaon","Gudvella","Patnagarh","Belpara",
        "Khaparakhol","Titilagarh","Muribahal","Saintala","Bongamunda","Tureikela","Tarva","Sonepur","Dunguripalli","Binika","Biramaharajpur","Ullunda",
        "Dhankhanda","Maneswar","Jujumura","Rengali","Rairakhol"," Naktideul","Kuchinda","Bamra","Jamankira","Bargarh","Barpalli","Attabira"," Bhatli",
        "Bheden"," Ambabhana","Rajborasambar","Paikmal","Jharabandha","Gaisilet","Sohela","Bijepur","Anadapur","Hatadihi","Ghasipur","Champua","Jhumpura",
        "Joda","Keonjhargarh","Harichandanpur","Patna","Ghatgaon","Saharpada","Telkoi","Banspal","Kuarmunda","Nuagaon","Bisra"," Lathikata","Lafripada",
        "Hemgiri","Rajgangpur","Kutra","Sundargarh","Bargaon","Subdega","Balisankara","Tangarpalli"," Lahunipada","Koira","Bonaigarh"," Gurundia",
        "Jharsuguda","Lakhanpur"," Kolabira","Laikera","Kirimira","Riamal","Barkote","Tileibani","Bhawanipatna","Kesinga","Narla","M.Rampur","Karlamunda",
        "Lanjigarh","ThumalRampur","Dharmagarh","Junagarh","Jaipatna","Koksara","Kalampur","Golamunda","Nawapara","Komna","Khariar","Sinapalli"," Boden",
        "Rangeilunda","Kukudakhandi","Digapahandi","Sankhemundi","Chikiti","Patrapur","Chhatrapur","Ganjam","Khalikote","Kodala"," Purusottampur",
        "Hinjilicut","Polsara","K.S.Nagar"," Bhanjanagar","Belguntha","Jagannathprasad","Buguda","Aska","Seragad","Dharakote","Surada","Kasinagar",
        " Paralakhemundi","Rayagada","Gumma","R.Udayagiri","Mohana","Nuagad"," Koraput","Similiguda","Pottangi","Laxmipur","Nandapur","Bandhugaon","Narayanpatna",
        "Lamtaput"," Dasmantpur","Jeypore","Kotpada","Kundara","Bariguma","Boipariguda","Malkangiri","Korkunda","Podia","Khairaput","Kudumuluguma",
        "Kalimela","Mathili","Rayagada","Kasipur","Kolnara","K.Singpur","Gunupur","Gudari","Bisam-Cuttack","Chandrapur","Muniguda"," Ramanguda","Padmapur",
        "Nawrangpur","Umerkote","Tentulikhunti","Chandahandi","Kosagumuda","Papadahandi","Jharigam","Dabugaon","Raighar","Nandahandi","Balliguda",
        "Chakpad","Daringibadi","G.Udayagiri","Kotgarh","Nuagaon","Raikia","Tikabali","Tumudibandh","Phulbani","Phiringia","Khajuripada","Boudh","Harabhanga",
        "Kantamal"];
        
        
        

        districtInput.addEventListener("input", function () {
            const searchQuery = districtInput.value.toLowerCase();
            const filteredDistricts = districts.filter(district =>
                district.toLowerCase().includes(searchQuery)
            );

            renderDistricts(filteredDistricts);
        });

        function renderDistricts(filteredDistricts) {
            districtList.innerHTML = "";

            filteredDistricts.forEach(district => {
                const districtItem = document.createElement("li");
                districtItem.textContent = district;
                districtItem.className = "district-item";

                districtItem.addEventListener("click", function () {
                    districtInput.value = district;
                    districtList.innerHTML = "";
                });

                districtList.appendChild(districtItem);
            });
        }
    });  