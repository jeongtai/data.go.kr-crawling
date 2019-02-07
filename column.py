
typeName = {
    #DUR품목정보서비스
        'getEfcyDplctInfoList' : '효능군중복',
        'getDurPrdlstInfoList' : 'DUR품목정보',
        'getSeobangjeongPartitnAtentInfoList' : '분할주의',
        'getOdsnAtentInfoList' : '노인주의',
        'getMdctnPdAtentInfoList': '투여기간주의',
        'getCpctyAtentInfoList' : '용량주의',
        'getPwnmTabooInfoList' : '임부금기',
        'getSpcifyAgrdeTabooInfoList' : '특정연령대금기',
        'getUsjntTabooInfoList' : '병용금기',
    #의약품성분약효정보조회서비스
        'getMajorCmpnNmCdList' : '주성분명칭코드목록조회',
    #건강기능식품 대상별 정보(DB) 서비스
        'getHtfsInfoList' : '건강기능식품 대상별 정보',
    #건강보험심사평가원 진료행위정보서비스
        'getMdlrtActionNameCodeList' : '진료행위명칭/코드조회',
        'getMdlrtActionByGenderAgeStats' : '진료행위성별연령별통계',
        'getMdlrtActionByClassesStats' : '진료행위의료기관종별통계',
        'getMdlrtActionByAreaStats' : '진료행위의료기관지역별통계/코드조회',
    #건강보험심사평가원 의료기관별상세정보서비스
        'getSpcHospAppnFieldList' : '전문병원지정분야',
        'getSpclMdlrtInfoList' : '특수진료정보(진료가능분야조회)',
        'getNursigGradeInfoList' : '간호등급정보',
        'getCgffdAddiInfoList' : '식대가산정보',
        'getMedicalEquipmentInfoList' : '의료장비정보',
        'getTransportInfoList' : '교통정보',
        'getMdlrtSbjectInfoList' : '진료과목정보',
        'getDetailInfo' : '세부정보',
        'getFacilityInfo' : '시설정보',
    ##건강보험심사평가원 병원정보 서비스
        #의료기관별상세정보서비스를 들고 오기 위한 암호코드(?)
        'getHospBasisList' : '병원기본 목록',
    #건강보험심사평가원 비급여진료비정보서비스
        'getNonPaymentItemHospList' : '비급여항목병원목록(‘16년 2월이전)',
        'getNonPaymentItemCodeList' : '비급여항목코드조회(‘16년 2월이전)',
        'getNonPaymentItemHospList2' : '비급여항목병원목록요약(‘16년3월이후)',
        'getNonPaymentItemCodeList2' : '비급여항목코드조회(‘16년 3월이후)',
        'getNonPaymentItemHospDtlList' : '비급여항목병원목록상세(‘16년3월이후)',
    #건강보험심사평가원 치료재료정보조회서비스
        'getPaymentNonPaymentList' : '급여비급여목록조회',
    #건강보험심사평가원 병원진료정보조회서비스
        'getClinicTop5List' : '의원진료상위질병5개목록조회'
        }

typeName_reverse = dict(zip(typeName.values(),typeName.keys()))

typeList= {
    "getEfcyDplctInfoList":{
      "TYPE_NAME": "타입유형",
      "DUR_SEQ": "DUR\uc77c\ub828\ubc88\ud638",
      "EFFECT_NAME": "\ud6a8\ub2a5",
      "INGR_CODE": "DUR\uc131\ubd84\ucf54\ub4dc",
      "INGR_NAME": "\uc131\ubd84\uba85",
      "INGR_ENG_NAME": "DUR\uc131\ubd84(\uc601\ubb38)",
      "FORM_CODE_NAME": "\uc81c\ud615\uad6c\ubd84",
      "MIX": "\ub2e8\uc77c/\ubcf5\ud569",
      "MIX_INGR": "\ubcf5\ud569\uc81c",
      "ITEM_SEQ": "\ud488\ubaa9\uae30\uc900\ucf54\ub4dc",
      "ITEM_NAME": "\ud488\ubaa9\uba85",
      "ITEM_PERMIT_DATE": "\ud488\ubaa9\ud5c8\uac00\uc77c\uc790",
      "CHART": "\uc131\uc0c1",
      "ENTP_NAME": "\uc5c5\uccb4\uba85",
      "FORM_CODE": "\uc81c\ud615\uad6c\ubd84\ucf54\ub4dc",
      "FORM_NAME": "\uc81c\ud615",
      "ETC_OTC_CODE": "\uc804\ubb38\uc77c\ubc18 \uad6c\ubd84\ucf54\ub4dc",
      "ETC_OTC_NAME": "\uc804\ubb38/\uc77c\ubc18",
      "CLASS_CODE": "\uc57d\ud6a8\ubd84\ub958\ucf54\ub4dc",
      "CLASS_NAME": "\uc57d\ud6a8\ubd84\ub958",
      "MAIN_INGR": "\uc8fc\uc131\ubd84",
      "NOTIFICATION_DATE": "\uace0\uc2dc\uc77c\uc790",
      "PROHBT_CONTENT": "\uae08\uae30\ub0b4\uc6a9",
      "REMARK": "\ube44\uace0",
      "INGR_ENG_NAME_FULL": "DUR\uc131\ubd84\uc0c1\uc138\uba85",
      "CHANGE_DATE": "\ubcc0\uacbd\uc77c\uc790"
    },
    "getMajorCmpnNmCdList": {
        'divNm': '분류명',
        'fomnTpCdNm': '제형구분명',
        'gnlNm': '일반명',
        'gnlNmCd': '일반명코드',
        'injcPthCdNm': '투여경로명',
        'iqtyTxt': '함량내용',
        'meftDivNo': '약효분류번호',
        'unit': '단위'
        },
    "getHtfsInfoList":{
        "PRDLST_NM": "\uc81c\ud488\uba85",
        "PRMS_DT": "\ub4f1\ub85d\uc77c\uc790",
        "DISPOS": "\uc131\uc0c1",
        "NTK_MTHD": "\uc12d\ucde8\ub7c9/\uc12d\ucde8\ubc29\ubc95",
        "CSTDY_MTHD": "\ubcf4\uc874 \ubc0f \uc720\ud1b5\uae30\uc900",
        "IFTKN_ATNT_MATR_CN": "\uc12d\ucde8\uc2dc \uc8fc\uc758\uc0ac\ud56d",
        "PRIMARY_FNCLTY": "\uae30\ub2a5\uc131 \ub0b4\uc6a9",
        "STDR_STND": "\uae30\uc900\ubc0f\uaddc\uaca9",
        "BSSH_NM": "\uc218\uc785\uc5c5\uccb4",
        "GU_PRDLST_MNF_MANAGE_NO": "\ud488\ubaa9\uc81c\uc870\uad00\ub9ac\ubc88\ud638"
        },
     "getMdlrtActionByAreaStats":{
      "execAmt01": "금액1",
      "execAmt02": "금액2",
      "execAmt03": "금액3",
      "execFq01": "실시횟수1",
      "execFq02": "실시횟수2",
      "execFq03": "실시횟수3",
      "lcName": "LC_NAME (지역)",
      "mdfeeCd": "수가코드",
      "mdfeeNm": "수가코드명",
      "pintCnt01": "환자수1",
      "pintCnt02": "환자수2",
      "pintCnt03": "환자수3",
    },
    'getDurPrdlstInfoList' : {
            'ITEM_SEQ': '품목기준코드',
            'ITEM_NAME': '품목명',
            'ENTP_NAME': '업체명',
            'ITEM_PERMIT_DATE': '허가일자',
            'ETC_OTC_CODE': '전문일반',
            'CLASS_NO': '분류',
            'CHART': '성상',
            'BAR_CODE': '표준코드',
            'MATERIAL_NAME': '원료성분',
            'EE_DOC_ID': '제조방법',
            'UD_DOC_ID': '용법용량',
            'NB_DOC_ID': '주의사항',
            'INSERT_FILE': '첨부문서',
            'STORAGE_METHOD': '저장방법',
            'VALID_TERM': '유효기간',
            'REEXAM_TARGET': '재심사대상',
            'REEXAM_DATE': '재심사기간',
            'PACK_UNIT': '포장단위',
            'EDI_CODE': '보험코드',
            'CANCEL_DATE': '취소일자',
            'CANCEL_NAME': '상태',
            'CHANGE_DATE': '변경일자'},
        'getSeobangjeongPartitnAtentInfoList' : {
            'TYPE_NAME': '타입 유형',
            'ITEM_SEQ': '품목기준코드',
            'ITEM_NAME': '품목명',
            'ITEM_PERMIT_DATE': '품목허가일자',
            'FORM_CODE_NAME': '제형코드이름',
            'ENTP_NAME': '업체명',
            'CHART': '성상',
            'CLASS_CODE': '약효분류코드',
            'CLASS_NAME': '약효분류',
            'ETC_OTC_NAME': '전문/일반',
            'MIX': '단일/복합',
            'MAIN_INGR': '주성분',
            'PROHBT_CONTENT': '금기내용',
            'REMARK': '비고',
            'CHANGE_DATE': '변경일자'},
        'getOdsnAtentInfoList' : {
            'TYPE_NAME': '타입유형',
            'MIX_TYPE': '단일/복합구분',
            'INGR_CODE': 'DUR성분코드',
            'INGR_ENG_NAME': 'DUR성분(영문)',
            'INGR_NAME': 'DUR성분(한글',
            'MIX_INGR': '복합제',
            'FORM_NAME': '형태',
            'ITEM_SEQ': '품목기준코드',
            'ITEM_NAME': '품목명',
            'ITEM_PERMIT_DATE': '품목허가일자',
            'ENTP_NAME': '업체명',
            'CHART': '성상',
            'CLASS_CODE': '약효분류코드',
            'CLASS_NAME': '약효분류',
            'ETC_OTC_NAME': '전문/일반',
            'MAIN_INGR': '주성분',
            'NOTIFICATION_DATE': '고시일자',
            'PROHBT_CONTENT': '금기내용',
            'REMARK': '비고',
            'INGR_ENG_NAME_FULL': 'DUR성분상세명',
            'CHANGE_DATE': '변경일자'},
        'getMdctnPdAtentInfoList' : {
            'TYPE_NAME': '타입유형',
            'MIX_TYPE': '단일/복합구분',
            'INGR_CODE': 'DUR성분코드',
            'INGR_ENG_NAME': 'DUR성분(영문)',
            'INGR_NAME': 'DUR성분(한글)',
            'MIX_INGR': '복합제',
            'FORM_NAME': '형태',
            'ITEM_SEQ': '품목기준코드',
            'ITEM_NAME': '품목명',
            'ITEM_PERMIT_DATE': '품목허가일자',
            'ENTP_NAME': '업체명',
            'CHART': '성상',
            'CLASS_CODE': '약효분류코드',
            'CLASS_NAME': '약효분류',
            'ETC_OTC_NAME': '전문/일반',
            'MAIN_INGR': '주성분',
            'NOTIFICATION_DATE': '고시일자',
            'PROHBT_CONTENT': '금기내용',
            'REMARK': '비고',
            'INGR_ENG_NAME_FULL': 'DUR성분상세명',
            'CHANGE_DATE': '변경일자'},
        'getCpctyAtentInfoList' : {
            'TYPE_NAME': '타입 유형',
            'MIX_TYPE': '단일/복합구분',
            'INGR_CODE': 'DUR성분코드',
            'INGR_ENG_NAME': 'DUR성분(영문)',
            'INGR_NAME': 'DUR성분(한글)',
            'MIX_INGR': '복합제',
            'FORM_NAME': '형태',
            'ITEM_SEQ': '품목기준코드',
            'ITEM_NAME': '품목명',
            'ITEM_PERMIT_DATE': '품목허가일자',
            'ENTP_NAME': '업체명',
            'CHART': '성상',
            'CLASS_CODE': '약효분류코드',
            'CLASS_NAME': '약효분류',
            'ETC_OTC_NAME': '전문/일반',
            'MAIN_INGR': '주성분',
            'NOTIFICATION_DATE': '고시일자',
            'PROHBT_CONTENT': '금기내용',
            'REMARK': '비고',
            'INGR_ENG_NAME_FULL': 'DUR성분상세명',
            'CHANGE_DATE': '변경일자'},
        'getPwnmTabooInfoList' : {
            'TYPE_NAME': '타입유형',
            'MIX_TYPE': '단일/복합구분',
            'INGR_CODE': 'DUR성분코드',
            'INGR_ENG_NAME': 'DUR성분(영문)',
            'INGR_NAME': 'DUR성분(한글)',
            'MIX_INGR': '복합제',
            'FORM_NAME': '형태',
            'ITEM_SEQ': '품목기준코드',
            'ITEM_NAME': '품목명',
            'ITEM_PERMIT_DATE': '품목허가일자',
            'ENTP_NAME': '업체명',
            'CHART': '성상',
            'CLASS_CODE': '약효분류코드',
            'CLASS_NAME': '약효분류',
            'ETC_OTC_NAME': '전문/일반',
            'MAIN_INGR': '주성분',
            'NOTIFICATION_DATE': '고시일자',
            'PROHBT_CONTENT': '금기내용',
            'REMARK': '비고',
            'INGR_ENG_NAME_FULL': 'DUR성분상세명',
            },
        'getSpcifyAgrdeTabooInfoList' : {
            'TYPE_NAME': '타입유형',
            'MIX_TYPE': '단일/복합구분',
            'INGR_CODE': 'DUR성분코드',
            'INGR_ENG_NAME': 'DUR성분(영문)',
            'INGR_NAME': 'DUR성분(한글)',
            'MIX_INGR': '복합제',
            'FORM_NAME': '형태',
            'ITEM_SEQ': '품목기준코드',
            'ITEM_NAME': '품목명',
            'ITEM_PERMIT_DATE': '품목허가일자',
            'ENTP_NAME': '업체명',
            'CHART': '성상',
            'CLASS_CODE': '약효분류코드',
            'CLASS_NAME': '약효분류',
            'ETC_OTC_NAME': '전문/일반',
            'MAIN_INGR': '주성분',
            'NOTIFICATION_DATE': '고시일자',
            'PROHBT_CONTENT': '금기내용',
            'REMARK': '비고',
            'INGR_ENG_NAME_FULL': 'DUR성분상세명',
            'CHANGE_DATE': '변경일자'},
        'getUsjntTabooInfoList' : {
            'TYPE_NAME': '타입유형',
            'DUR_SEQ': 'DUR일련번호',
            'TYPE_CODE': 'DUR유형코드',
            'MIX': '단일/복합',
            'INGR_CODE': 'DUR성분코드',
            'INGR_KOR_NAME': 'DUR성분',
            'INGR_ENG_NAME': 'DUR성분(영문)',
            'MIX_INGR': '복합제',
            'ITEM_SEQ': '품목기준코드',
            'ITEM_NAME': '품목명',
            'ENTP_NAME': '업체명',
            'CHART': '성상',
            'FORM_CODE': '제형구분코드',
            'ETC_OTC_CODE': '전문일반 구분코드',
            'CLASS_CODE': '약효분류코드',
            'FORM_NAME': '제형',
            'ETC_OTC_NAME': '전문/일반',
            'CLASS_NAME': '약효분류',
            'MAIN_INGR': '주성분',
            'MIXTURE_DUR_SEQ': '병용금기DUR번호',
            'MIXTURE_MIX': '병용금기복합제',
            'MIXTURE_INGR_CODE': '병용금기DUR성분코드',
            'MIXTURE_INGR_KOR_NAME': '병용금기DUR성분',
            'MIXTURE_INGR_ENG_NAME': '병용금기DUR성분(영문)',
            'MIXTURE_ITEM_SEQ': '병용금기품목기준코드',
            'MIXTURE_ITEM_NAME': '병용금기품목명',
            'MIXTURE_ENTP_NAME': '병용금기업체명',
            'MIXTURE_FORM_CODE': '병용금기제형구분코드',
            'MIXTURE_ETC_OTC_CODE': '병용금기전문일반구분코드',
            'MIXTURE_CLASS_CODE': '병용금기약효분류코드',
            'MIXTURE_FORM_NAME': '병용금기제형',
            'MIXTURE_ETC_OTC_NAME': '병용금기전문/일반',
            'MIXTURE_CLASS_NAME': '병용금기약효분류',
            'MIXTURE_MAIN_INGR': '병용금기주성분',
            'NOTIFICATION_DATE': '고시일자',
            'PROHBT_CONTENT': '금기내용',
            'REMARK': '비고',
            'ITEM_PERMIT_DATE': '품목허가일자',
            'MIXTURE_ITEM_PERMIT_DATE': '병용금기품목허가일자',
            'MIXTURE_CHART': '병용금기성상',
            'CHANGE_DATE': '변경일자',
            'MIXTURE_CHANGE_DATE': '병용변경일자'},
        "getMdlrtActionByGenderAgeStats" : {
          "age": "연령",
          "execAmt01": "금액1",
          "execAmt02": "금액2",
          "execAmt03": "금액3",
          "execFq01": "실시횟수1",
          "execFq02": "실시횟수2",
          "execFq03": "실시횟수3",
          "pintCnt01": "환자수1",
          "pintCnt02": "환자수2",
          "pintCnt03": "환자수3",
          "sex": "성별",
          "mdfeeCd": "수가코드",
          "mdfeeNm": "수가코드명"
        },
        "getMdlrtActionNameCodeList" : {
            "mdfeeCd" : "수가코드",
            "mdfeeNm" : "수가코드명"
        },
         "getMdlrtActionByClassesStats" : {
            "execAmt01" : "금액1",
            "execAmt02" : "금액2",
            "execAmt03" : "금액3",
            "execFq01" : "실시횟수1",
            "execFq02" : "실시횟"
                         "수2",
            "execFq03": "실시횟수3",
            "grade": "등급",
            "mdfeeCd": "수가코드",
            "mdfeeNm": "수가코드명",
            "pintCnt01": "환자수1",
            "pintCnt02": "환자수2",
            "pintCnt03": "환자수3"
        },
        "getSpcHospAppnFieldList" : {
            "srchCd" : "구분 코드",
            "srchCdNm" : "구분 코드명"
        },
        "getSpclMdlrtInfoList": {
            "srchCd": "구분 코드",
            "srchCdNm": "구분 코드명"
        },
        "getNursigGradeInfoList": {
            "tyCd": "구분 코드",
            "tyCdNm": "구분 코드명",
            "careGrd" : "간호등급"
        },
        "getCgffdAddiInfoList": {
            "tyCd": "구분 코드",
            "tyCdNm": "구분 코드명",
            "careGrd" : "일반식 가산 적용여부",
            "calcNopCnt" : "인원수",
            "trmealGrd" : "등급"
        },
        "getMedicalEquipmentInfoList": {
            "tyCd": "장비코드",
            "tyCdNm": "장비명",
            "careGrd" : "보유대수"
        },
        "getTransportInfoList":{
          "trafNm": "\uad50\ud1b5\ud3b8",
          "lineNo": "\ub178\uc120\ubc88\ud638",
          "arivPlc": "\ud558\ucc28\uc9c0\uc810",
          "dir": "\ubc29\ud5a5",
          "dist": "\uac70\ub9ac",
          "rmk": "\ube44\uace0"
        },
        "getMdlrtSbjectInfoList":{
          "dgsbjtCd": "\uc9c4\ub8cc\uacfc\ubaa9\ucf54\ub4dc",
          "dgsbjtCdNm": "\uc9c4\ub8cc\uacfc\ubaa9\ucf54\ub4dc\uba85",
          "dgsbjtPrSdrCnt": "\uc758\uc0ac\uc218",
          "cdiagDrCnt": "\uc120\ud0dd\uc9c4\ub8cc\uc758\uc0ac\uc218"
        },
        "getDetailInfo":{
          "plcNm": "\uacf5\uacf5\uac74\ubb3c(\uc7a5\uc18c) \uc774\ub984",
          "plcDir": "\uacf5\uacf5\uac74\ubb3c(\uc7a5\uc18c) \ubc29\ud5a5",
          "plcDist": "\uacf5\uacf5\uac74\ubb3c(\uc7a5\uc18c) \uac70\ub9ac",
          "parkQty": "\uc8fc\ucc28 \uac00\ub2a5\ub300\uc218",
          "parkXpnsYn": "\uc8fc\ucc28\uc7a5 \uc6b4\uc601\uc5ec\ubd80, \uc8fc\ucc28\ube44\uc6a9 \ubd80\ub2f4\uc5ec\ubd80",
          "parkEtc": "\uae30\ud0c0 \uc548\ub0b4\uc0ac\ud56d",
          "noTrmtSun": "\uc77c\uc694\uc77c \ud734\uc9c4 \uc548\ub0b4",
          "noTrmtHoli": "\uacf5\ud734\uc77c \ud734\uc9c4 \uc548\ub0b4",
          "emyDayYn": "\uc8fc\uac04 \uc751\uae09\uc2e4 \uc6b4\uc601\uc5ec\ubd80",
          "emyDayTelNo1": "\uc8fc\uac04 \uc751\uae09\uc2e4 \uc804\ud654\ubc88\ud638 1",
          "emyDayTelNo2": "\uc8fc\uac04 \uc751\uae09\uc2e4 \uc804\ud654\ubc88\ud638 2",
          "emyNgtYn": "\uc57c\uac04 \uc751\uae09\uc2e4 \uc6b4\uc601\uc5ec\ubd80",
          "emyNgtTelNo1": "emyNgtTelNo1\t\uc57c\uac04 \uc751\uae09\uc2e4 \uc804\ud654\ubc88\ud638 1",
          "emyNgtTelNo2": "emyNgtTelNo1\t\uc57c\uac04 \uc751\uae09\uc2e4 \uc804\ud654\ubc88\ud638 2",
          "lunchWeek": "\uc6d4~\uae08 \uc810\uc2ec\uc2dc\uac04"
        },
        "getFacilityInfo": {
            "yadmNm": "병원명",
            "clCd": "종별 코드",
            "clCdNm": "종별 코드명",
            "orgTyCd": "설립 구분",
            "orgTyCdNm": "설립 구분명",
            "sidoCd": "시도코드",
            "sidoCdNm": "시도명",
            "sgguCd": "시군구코드",
            "sgguCdNm": "시군구명",
            "emdongNm": "읍면동명",
            "postNo": "우편번호",
            "addr": "주소",
            "telno": "전화번호",
            "hghrSickbdCnt": "상급 입원실(병상수)",
            "stdSickbdCnt": "일반 입원실(병상수)",
            "aduChldSprmCnt": "성인/소아 중환자실(병상수)",
            "nbySprmCnt": "신생아 중환자실(병상수)",
            "partumCnt": "분만실(병상수)",
            "soprmCnt": "수술실(병상수)",
            "emymCnt": "응급실(병상수)",
            "ptrmCnt": "물리치료실(병상수)",
            "hospUrl": "홈페이지",
            "estbDd": "개설일자"
        },
        "getHospBasisList":{
          # "XPos": "x\uc88c\ud45c",
          # "YPos": "y\uc88c\ud45c",
          # "estbDd": "\uac1c\uc124\uc77c\uc790",
          # "postNo": "\uc6b0\ud3b8\ubc88\ud638",
          # "hospUrl": "\ud648\ud398\uc774\uc9c0",
          # "emdongNm": "\uc74d\uba74\ub3d9\uba85",
          # "clCd": "\uc885\ubcc4\ucf54\ub4dc",
            "ykiho": "\uc554\ud638\ud654\ub41c \uc694\uc591\uae30\ud638",
          # "telno": "\uc804\ud654\ubc88\ud638",
          # "clCdNm": "\uc885\ubcc4\ucf54\ub4dc\uba85",
          # "sdrCnt": "\uc804\ubb38\uc758 \uc778\uc6d0\uc218",
          # "yadmNm": "\ubcd1\uc6d0\uba85",
          # "sidoCd": "\uc2dc\ub3c4\ucf54\ub4dc",
          # "sidoCdNm": "\uc2dc\ub3c4\uba85",
          # "distance": "\uac70\ub9ac",
          # "sgguCd": "\uc2dc\uad70\uad6c\ucf54\ub4dc",
          # "sgguCdNm": "\uc2dc\uad70\uad6c\uba85",
          # "resdntCnt": "\ub808\uc9c0\ub358\ud2b8 \uc778\uc6d0\uc218",
          # "addr": "\uc8fc\uc18c",
          # "drTotCnt": "\uc758\uc0ac\ucd1d\uc218",
          # "gdrCnt": "\uc77c\ubc18\uc758 \uc778\uc6d0\uc218",
          # "intnCnt" : "인턴 인원수",
        },

        "getNonPaymentItemHospList": {
            "clCd": "종별코드(병원구분코드)",
            "clCdNm": "종별코드명(병원구분)",
            "divCd1": "1차분류코드(항목명코드)",
            "divCd1Nm": "1차분류코드명(항목명)",
            "divCd2": "2차분류코드(중분류코드)",
            "divCd2Nm": "2차분류코드명(중분류)",
            "divCd3": "3차분류코드",
            "divCd3Nm": "3차분류코드명",
            "invtDt": "기준일",
            "itmCd": "항목코드",
            "itmCdNm": "항목코드명(병원사용명칭)",
            "itmPrcMax": "항목의 최대비용",
            "itmPrcMin": "항목의 최소비용",
            "prcMax": "최대비용",
            "prcMin": "최소비용",
            "rmk1": "비고1",
            "sgguCd": "시군구코드",
            "sgguCdNm": "시군구명",
            "sidoCd": "시도코드",
            "sidoCdNm": "시도명",
            "url": "확인URL",
            "yadmNm": "병원명",
            "ykiho": "암호화된 요양기호"
        },
        "getNonPaymentItemHospList2": {
            "ykiho": "암호화된 요양기호",
            "yadm_nm": "병원명",
            "cl_cd": "종별코드",
            "cl_cd_nm": "종별코드명",
            "sido_cd": "시도코드",
            "sido_cd_nm": "시도명",
            "sggu_cd": "시군구코드",
            "sggu_cd_nm": "시군구명",
            "url_addr": "URL주소",
            "npay_cd": "비급여코드",
            "npay_kor_nm": "비급여한글명",
            "npay_mdiv_cd": "비급여중분류코드",
            "npay_mdiv_cd_nm": "비급여중분류코드명",
            "npay_sdiv_cd": "비급여소분류코드",
            "npay_sdiv_cd_nm": "비급여소분류코드명",
            "npay_dtl_div_cd": "비급여상세분류코드",
            "npay_dtl_div_cd_nm": "시군구코드",
            "sgguCdNm": "비급여상세분류코드명",
            "adt_fr_dd": "적용개시일자",
            "adt_end_dd": "적용종료일자",
            "min_prc": "최소가격",
            "max_prc": "최대비용",
        },
        "getNonPaymentItemCodeList" : {
            "divCd1": "1차분류코드",
            "divCd1Nm": "1차분류코드명",
            "divCd1Dsc": "1차분류코드설명",
            "divCd2": "2차분류코드",
            "divCd2Nm": "2차분류코드명",
            "divCd2Dsc": "2차분류코드설명",
            "divCd3": "3차분류코드",
            "divCd3Nm": "3차분류코드명",
            "divCd3Dsc": "3차분류코드설명",
        },
        "getNonPaymentItemCodeList2" : {
            "npay_cd": "비급여코드",
            "npay_kor_nm": "비급여한글명",
            "npay_mdiv_cd": "비급여중분류코드",
            "npay_mdiv_cd_nm": "비급여중분류코드명",
            "npay_sdiv_cd": "비급여소분류코드",
            "npay_sdiv_cd_nm": "비급여소분류코드명",
            "npay_dtl_div_cd": "비급여상세분류코드",
            "npay_dtl_div_cd_nm": "비급여상세분류코드명",
            "cmmt_txt": "비급여상세분류코드명",
            "ADT_FR_DD": "적용개시일자",
            "ADT_END_DD": "적용종료일자",
        },
        "getNonPaymentItemHospDtlList" : {
            "ykiho": "암호화된 요양기호",
            "yadm_nm": "병원명",
            "cl_cd": "종별코드",
            "cl_cd_nm": "종별코드명",
            "sido_cd": "시도코드",
            "sido_cd_nm": "시도명",
            "sggu_cd": "시군구코드",
            "sggu_cd_nm": "시군구명",
            "url_addr": "URL주소",
            "sno": "일련번호",
            "npay_cd": "비급여코드",
            "npay_kor_nm": "비급여한글명",
            "yadm_npay_cd_nm": "요양기관비급여코드명",
            "adt_fr_dd": "적용개시일자",
            "adt_end_dd": "적용종료일자",
            "cur_amt": "현재금액",
        },
         "getPaymentNonPaymentList": {
            "impEntpNm": "수입업체명",
            "itmNm": "품목명",
            "ldgrpCd": "대분류군코드",
            "ldgrpCdNm": "대분류군코드명",
            "ldivCd": "대분류코드",
            "ldivCdNm": "대분류코드명",
            "mcatCd": "재료대코드",
            "mdivCdNm": "중분류코드명",
            "mnfEntpNm": "제조업체명",
            "mxUnprc": "상한단가",
            "nomNm": "규격명",
            "payTpNm": "급여구분명",
            "unit": "단위"
        },
        "getClinicTop5List" : {
            "crtrYm": "기준년월",
            "mfrnIntrsIlnsNm1": "국민관심질병명1",
            "mfrnIntrsIlnsNm2": "국민관심질병명2",
            "mfrnIntrsIlnsNm3": "국민관심질병명3",
            "mfrnIntrsIlnsNm4": "국민관심질병명4",
            "mfrnIntrsIlnsNm5": "국민관심질병명5",
            "shwSbjtNm": "표시과목명",
            "yadmNm": "요양기관명",
            "ykiho": "암호화된 요양기호"
        }


}

typeName = {
    #DUR품목정보서비스
        'getEfcyDplctInfoList' : '효능군중복',
        'getDurPrdlstInfoList' : 'DUR품목정보',
        'getSeobangjeongPartitnAtentInfoList' : '분할주의',
        'getOdsnAtentInfoList' : '노인주의',
        'getMdctnPdAtentInfoList': '투여기간주의',
        'getCpctyAtentInfoList' : '용량주의',
        'getPwnmTabooInfoList' : '임부금기',
        'getSpcifyAgrdeTabooInfoList' : '특정연령대금기',
        'getUsjntTabooInfoList' : '병용금기',
    #의약품성분약효정보조회서비스
        'getMajorCmpnNmCdList' : '주성분명칭코드목록조회',
    #건강기능식품 대상별 정보(DB) 서비스
        'getHtfsInfoList' : '건강기능식품 대상별 정보',
    #건강보험심사평가원 진료행위정보서비스
        'getMdlrtActionByAreaStats' : '진료행위의료기관지역별통계',
        'getMdlrtActionByClassesStats' : '진료행위의료기관종별통계',
        'getMdlrtActionByGenderAgeStats' : '진료행위성별연령별통계',
        'getMdlrtActionNameCodeList' : '진료행위명칭/코드조회',
    #건강보험심사평가원 의료기관별상세정보서비스
        'getSpcHospAppnFieldList' : '전문병원지정분야',
        'getSpclMdlrtInfoList' : '특수진료정보(진료가능분야조회)',
        'getNursigGradeInfoList' : '간호등급정보',
        'getCgffdAddiInfoList' : '식대가산정보',
        'getMedicalEquipmentInfoList' : '의료장비정보',
        'getTransportInfoList' : '교통정보',
        'getMdlrtSbjectInfoList' : '진료과목정보',
        'getDetailInfo' : '세부정보',
        'getFacilityInfo' : '시설정보',
    #건강보험심사평가원 비급여진료비정보서비스
        'getNonPaymentItemHospList' : '비급여항목병원목록',
        'getNonPaymentItemCodeList' : '비급여항목코드조회',
    #건강보험심사평가원 치료재료정보조회서비스
        'getPaymentNonPaymentList' : '급여비급여목록조회',
    #건강보험심사평가원 병원진료정보조회서비스
        'getClinicTop5List' : '의원진료상위질병5개목록조회'
        }

typeName_reverse = dict(zip(typeName.values(),typeName.keys()))

typeList= {
    "getEfcyDplctInfoList":{
      "TYPE_NAME": "타입유형",
      "DUR_SEQ": "DUR\uc77c\ub828\ubc88\ud638",
      "EFFECT_NAME": "\ud6a8\ub2a5",
      "INGR_CODE": "DUR\uc131\ubd84\ucf54\ub4dc",
      "INGR_NAME": "\uc131\ubd84\uba85",
      "INGR_ENG_NAME": "DUR\uc131\ubd84(\uc601\ubb38)",
      "FORM_CODE_NAME": "\uc81c\ud615\uad6c\ubd84",
      "MIX": "\ub2e8\uc77c/\ubcf5\ud569",
      "MIX_INGR": "\ubcf5\ud569\uc81c",
      "ITEM_SEQ": "\ud488\ubaa9\uae30\uc900\ucf54\ub4dc",
      "ITEM_NAME": "\ud488\ubaa9\uba85",
      "ITEM_PERMIT_DATE": "\ud488\ubaa9\ud5c8\uac00\uc77c\uc790",
      "CHART": "\uc131\uc0c1",
      "ENTP_NAME": "\uc5c5\uccb4\uba85",
      "FORM_CODE": "\uc81c\ud615\uad6c\ubd84\ucf54\ub4dc",
      "FORM_NAME": "\uc81c\ud615",
      "ETC_OTC_CODE": "\uc804\ubb38\uc77c\ubc18 \uad6c\ubd84\ucf54\ub4dc",
      "ETC_OTC_NAME": "\uc804\ubb38/\uc77c\ubc18",
      "CLASS_CODE": "\uc57d\ud6a8\ubd84\ub958\ucf54\ub4dc",
      "CLASS_NAME": "\uc57d\ud6a8\ubd84\ub958",
      "MAIN_INGR": "\uc8fc\uc131\ubd84",
      "NOTIFICATION_DATE": "\uace0\uc2dc\uc77c\uc790",
      "PROHBT_CONTENT": "\uae08\uae30\ub0b4\uc6a9",
      "REMARK": "\ube44\uace0",
      "INGR_ENG_NAME_FULL": "DUR\uc131\ubd84\uc0c1\uc138\uba85",
      "CHANGE_DATE": "\ubcc0\uacbd\uc77c\uc790"
    },
    "getMajorCmpnNmCdList": {
        'divNm': '분류명',
        'fomnTpCdNm': '제형구분명',
        'gnlNm': '일반명',
        'gnlNmCd': '일반명코드',
        'injcPthCdNm': '투여경로명',
        'iqtyTxt': '함량내용',
        'meftDivNo': '약효분류번호',
        'unit': '단위'
        },
    "getHtfsInfoList":{
        "PRDLST_NM": "\uc81c\ud488\uba85",
        "PRMS_DT": "\ub4f1\ub85d\uc77c\uc790",
        "DISPOS": "\uc131\uc0c1",
        "NTK_MTHD": "\uc12d\ucde8\ub7c9/\uc12d\ucde8\ubc29\ubc95",
        "CSTDY_MTHD": "\ubcf4\uc874 \ubc0f \uc720\ud1b5\uae30\uc900",
        "IFTKN_ATNT_MATR_CN": "\uc12d\ucde8\uc2dc \uc8fc\uc758\uc0ac\ud56d",
        "PRIMARY_FNCLTY": "\uae30\ub2a5\uc131 \ub0b4\uc6a9",
        "STDR_STND": "\uae30\uc900\ubc0f\uaddc\uaca9",
        "BSSH_NM": "\uc218\uc785\uc5c5\uccb4",
        "GU_PRDLST_MNF_MANAGE_NO": "\ud488\ubaa9\uc81c\uc870\uad00\ub9ac\ubc88\ud638"
        },
     "getMdlrtActionByAreaStats":{
      "execAmt01": "\uae08\uc5611",
      "execAmt02": "\uae08\uc5612",
      "execAmt03": "\uae08\uc5613",
      "execFq01": "\uc2e4\uc2dc\ud69f\uc2181",
      "execFq02": "\uc2e4\uc2dc\ud69f\uc2182",
      "execFq03": "\uc2e4\uc2dc\ud69f\uc2183",
      "lcName": "LC_NAME (\uc9c0\uc5ed)",
      "mdfeeCd": "\uc218\uac00\ucf54\ub4dc",
      "mdfeeNm": "\uc218\uac00\ucf54\ub4dc\uba85",
      "pintCnt01": "\ud658\uc790\uc2181",
      "pintCnt02": "\ud658\uc790\uc2182",
      "pintCnt03": "\ud658\uc790\uc2183"
    },
    'getDurPrdlstInfoList' : {
            'ITEM_SEQ': '품목기준코드',
            'ITEM_NAME': '품목명',
            'ENTP_NAME': '업체명',
            'ITEM_PERMIT_DATE': '허가일자',
            'ETC_OTC_CODE': '전문일반',
            'CLASS_NO': '분류',
            'CHART': '성상',
            'BAR_CODE': '표준코드',
            'MATERIAL_NAME': '원료성분',
            'EE_DOC_ID': '제조방법',
            'UD_DOC_ID': '용법용량',
            'NB_DOC_ID': '주의사항',
            'INSERT_FILE': '첨부문서',
            'STORAGE_METHOD': '저장방법',
            'VALID_TERM': '유효기간',
            'REEXAM_TARGET': '재심사대상',
            'REEXAM_DATE': '재심사기간',
            'PACK_UNIT': '포장단위',
            'EDI_CODE': '보험코드',
            'CANCEL_DATE': '취소일자',
            'CANCEL_NAME': '상태',
            'CHANGE_DATE': '변경일자'},
        'getSeobangjeongPartitnAtentInfoList' : {
            'TYPE_NAME': '타입 유형',
            'ITEM_SEQ': '품목기준코드',
            'ITEM_NAME': '품목명',
            'ITEM_PERMIT_DATE': '품목허가일자',
            'FORM_CODE_NAME': '제형코드이름',
            'ENTP_NAME': '업체명',
            'CHART': '성상',
            'CLASS_CODE': '약효분류코드',
            'CLASS_NAME': '약효분류',
            'ETC_OTC_NAME': '전문/일반',
            'MIX': '단일/복합',
            'MAIN_INGR': '주성분',
            'PROHBT_CONTENT': '금기내용',
            'REMARK': '비고',
            'CHANGE_DATE': '변경일자'},
        'getOdsnAtentInfoList' : {
            'TYPE_NAME': '타입유형',
            'MIX_TYPE': '단일/복합구분',
            'INGR_CODE': 'DUR성분코드',
            'INGR_ENG_NAME': 'DUR성분(영문)',
            'INGR_NAME': 'DUR성분(한글',
            'MIX_INGR': '복합제',
            'FORM_NAME': '형태',
            'ITEM_SEQ': '품목기준코드',
            'ITEM_NAME': '품목명',
            'ITEM_PERMIT_DATE': '품목허가일자',
            'ENTP_NAME': '업체명',
            'CHART': '성상',
            'CLASS_CODE': '약효분류코드',
            'CLASS_NAME': '약효분류',
            'ETC_OTC_NAME': '전문/일반',
            'MAIN_INGR': '주성분',
            'NOTIFICATION_DATE': '고시일자',
            'PROHBT_CONTENT': '금기내용',
            'REMARK': '비고',
            'INGR_ENG_NAME_FULL': 'DUR성분상세명',
            'CHANGE_DATE': '변경일자'},
        'getMdctnPdAtentInfoList' : {
            'TYPE_NAME': '타입유형',
            'MIX_TYPE': '단일/복합구분',
            'INGR_CODE': 'DUR성분코드',
            'INGR_ENG_NAME': 'DUR성분(영문)',
            'INGR_NAME': 'DUR성분(한글)',
            'MIX_INGR': '복합제',
            'FORM_NAME': '형태',
            'ITEM_SEQ': '품목기준코드',
            'ITEM_NAME': '품목명',
            'ITEM_PERMIT_DATE': '품목허가일자',
            'ENTP_NAME': '업체명',
            'CHART': '성상',
            'CLASS_CODE': '약효분류코드',
            'CLASS_NAME': '약효분류',
            'ETC_OTC_NAME': '전문/일반',
            'MAIN_INGR': '주성분',
            'NOTIFICATION_DATE': '고시일자',
            'PROHBT_CONTENT': '금기내용',
            'REMARK': '비고',
            'INGR_ENG_NAME_FULL': 'DUR성분상세명',
            'CHANGE_DATE': '변경일자'},
        'getCpctyAtentInfoList' : {
            'TYPE_NAME': '타입 유형',
            'MIX_TYPE': '단일/복합구분',
            'INGR_CODE': 'DUR성분코드',
            'INGR_ENG_NAME': 'DUR성분(영문)',
            'INGR_NAME': 'DUR성분(한글)',
            'MIX_INGR': '복합제',
            'FORM_NAME': '형태',
            'ITEM_SEQ': '품목기준코드',
            'ITEM_NAME': '품목명',
            'ITEM_PERMIT_DATE': '품목허가일자',
            'ENTP_NAME': '업체명',
            'CHART': '성상',
            'CLASS_CODE': '약효분류코드',
            'CLASS_NAME': '약효분류',
            'ETC_OTC_NAME': '전문/일반',
            'MAIN_INGR': '주성분',
            'NOTIFICATION_DATE': '고시일자',
            'PROHBT_CONTENT': '금기내용',
            'REMARK': '비고',
            'INGR_ENG_NAME_FULL': 'DUR성분상세명',
            'CHANGE_DATE': '변경일자'},
        'getPwnmTabooInfoList' : {
            'TYPE_NAME': '타입유형',
            'MIX_TYPE': '단일/복합구분',
            'INGR_CODE': 'DUR성분코드',
            'INGR_ENG_NAME': 'DUR성분(영문)',
            'INGR_NAME': 'DUR성분(한글)',
            'MIX_INGR': '복합제',
            'FORM_NAME': '형태',
            'ITEM_SEQ': '품목기준코드',
            'ITEM_NAME': '품목명',
            'ITEM_PERMIT_DATE': '품목허가일자',
            'ENTP_NAME': '업체명',
            'CHART': '성상',
            'CLASS_CODE': '약효분류코드',
            'CLASS_NAME': '약효분류',
            'ETC_OTC_NAME': '전문/일반',
            'MAIN_INGR': '주성분',
            'NOTIFICATION_DATE': '고시일자',
            'PROHBT_CONTENT': '금기내용',
            'REMARK': '비고',
            'INGR_ENG_NAME_FULL': 'DUR성분상세명'
            },
        'getSpcifyAgrdeTabooInfoList' : {
            'TYPE_NAME': '타입유형',
            'MIX_TYPE': '단일/복합구분',
            'INGR_CODE': 'DUR성분코드',
            'INGR_ENG_NAME': 'DUR성분(영문)',
            'INGR_NAME': 'DUR성분(한글)',
            'MIX_INGR': '복합제',
            'FORM_NAME': '형태',
            'ITEM_SEQ': '품목기준코드',
            'ITEM_NAME': '품목명',
            'ITEM_PERMIT_DATE': '품목허가일자',
            'ENTP_NAME': '업체명',
            'CHART': '성상',
            'CLASS_CODE': '약효분류코드',
            'CLASS_NAME': '약효분류',
            'ETC_OTC_NAME': '전문/일반',
            'MAIN_INGR': '주성분',
            'NOTIFICATION_DATE': '고시일자',
            'PROHBT_CONTENT': '금기내용',
            'REMARK': '비고',
            'INGR_ENG_NAME_FULL': 'DUR성분상세명',
            'CHANGE_DATE': '변경일자'},
        'getUsjntTabooInfoList' : {
            'TYPE_NAME': '타입유형',
            'DUR_SEQ': 'DUR일련번호',
            'TYPE_CODE': 'DUR유형코드',
            'MIX': '단일/복합',
            'INGR_CODE': 'DUR성분코드',
            'INGR_KOR_NAME': 'DUR성분',
            'INGR_ENG_NAME': 'DUR성분(영문)',
            'MIX_INGR': '복합제',
            'ITEM_SEQ': '품목기준코드',
            'ITEM_NAME': '품목명',
            'ENTP_NAME': '업체명',
            'CHART': '성상',
            'FORM_CODE': '제형구분코드',
            'ETC_OTC_CODE': '전문일반 구분코드',
            'CLASS_CODE': '약효분류코드',
            'FORM_NAME': '제형',
            'ETC_OTC_NAME': '전문/일반',
            'CLASS_NAME': '약효분류',
            'MAIN_INGR': '주성분',
            'MIXTURE_DUR_SEQ': '병용금기DUR번호',
            'MIXTURE_MIX': '병용금기복합제',
            'MIXTURE_INGR_CODE': '병용금기DUR성분코드',
            'MIXTURE_INGR_KOR_NAME': '병용금기DUR성분',
            'MIXTURE_INGR_ENG_NAME': '병용금기DUR성분(영문)',
            'MIXTURE_ITEM_SEQ': '병용금기품목기준코드',
            'MIXTURE_ITEM_NAME': '병용금기품목명',
            'MIXTURE_ENTP_NAME': '병용금기업체명',
            'MIXTURE_FORM_CODE': '병용금기제형구분코드',
            'MIXTURE_ETC_OTC_CODE': '병용금기전문일반구분코드',
            'MIXTURE_CLASS_CODE': '병용금기약효분류코드',
            'MIXTURE_FORM_NAME': '병용금기제형',
            'MIXTURE_ETC_OTC_NAME': '병용금기전문/일반',
            'MIXTURE_CLASS_NAME': '병용금기약효분류',
            'MIXTURE_MAIN_INGR': '병용금기주성분',
            'NOTIFICATION_DATE': '고시일자',
            'PROHBT_CONTENT': '금기내용',
            'REMARK': '비고',
            'ITEM_PERMIT_DATE': '품목허가일자',
            'MIXTURE_ITEM_PERMIT_DATE': '병용금기품목허가일자',
            'MIXTURE_CHART': '병용금기성상',
            'CHANGE_DATE': '변경일자',
            'MIXTURE_CHANGE_DATE': '병용변경일자'},
        "getMdlrtActionByGenderAgeStats":{
          "age": "\uc5f0\ub839",
          "execAmt01": "\uae08\uc5611",
          "execAmt02": "\uae08\uc5612",
          "execAmt03": "\uae08\uc5613",
          "execFq01": "\uc2e4\uc2dc\ud69f\uc2181",
          "execFq02": "\uc2e4\uc2dc\ud69f\uc2182",
          "execFq03": "\uc2e4\uc2dc\ud69f\uc2183",
          "pintCnt01": "\ud658\uc790\uc2181",
          "pintCnt02": "\ud658\uc790\uc2182",
          "pintCnt03": "\ud658\uc790\uc2183",
          "sex": "\uc131\ubcc4",
          "mdfeeCd": "\uc218\uac00\ucf54\ub4dc",
          "mdfeeNm": "\uc218\uac00\ucf54\ub4dc\uba85"
        },
        "getMdlrtActionNameCodeList" : {
            "mdfeeCd" : "수가코드",
            "mdfeeNm" : "수가코드명"
        },
         "getMdlrtActionByClassesStats" : {
            "execAmt01" : "금액1",
            "execAmt02" : "금액2",
            "execAmt03" : "금액3",
            "execFq01" : "실시횟수1",
            "execFq02" : "실시횟수2",
            "execFq03": "실시횟수3",
            "grade": "등급",
            "mdfeeCd": "수가코드",
            "mdfeeNm": "수가코드명",
            "pintCnt01": "환자수1",
            "pintCnt02": "환자수2",
            "pintCnt03": "환자수3"
        },
        "getSpcHospAppnFieldList" : {
            "srchCd" : "구분 코드",
            "srchCdNm" : "구분 코드명"
        },
        "getSpclMdlrtInfoList": {
            "srchCd": "구분 코드",
            "srchCdNm": "구분 코드명"
        },
        "getNursigGradeInfoList": {
            "tyCd": "구분 코드",
            "tyCdNm": "구분 코드명",
            "careGrd" : "간호등급"
        },
        "getCgffdAddiInfoList": {
            "tyCd": "구분 코드",
            "tyCdNm": "구분 코드명",
            "careGrd" : "일반식 가산 적용여부",
            "calcNopCnt" : "인원수",
            "trmealGrd" : "등급"
        },
        "getMedicalEquipmentInfoList": {
            "tyCd": "장비코드",
            "tyCdNm": "장비명",
            "careGrd" : "보유대수"
        },
        "getTransportInfoList":{
          "trafNm": "\uad50\ud1b5\ud3b8",
          "lineNo": "\ub178\uc120\ubc88\ud638",
          "arivPlc": "\ud558\ucc28\uc9c0\uc810",
          "dir": "\ubc29\ud5a5",
          "dist": "\uac70\ub9ac",
          "rmk": "\ube44\uace0"
        },
        "getMdlrtSbjectInfoList":{
          "dgsbjtCd": "\uc9c4\ub8cc\uacfc\ubaa9\ucf54\ub4dc",
          "dgsbjtCdNm": "\uc9c4\ub8cc\uacfc\ubaa9\ucf54\ub4dc\uba85",
          "dgsbjtPrSdrCnt": "\uc758\uc0ac\uc218",
          "cdiagDrCnt": "\uc120\ud0dd\uc9c4\ub8cc\uc758\uc0ac\uc218"
        },
        "getDetailInfo":{
          "plcNm": "\uacf5\uacf5\uac74\ubb3c(\uc7a5\uc18c) \uc774\ub984",
          "plcDir": "\uacf5\uacf5\uac74\ubb3c(\uc7a5\uc18c) \ubc29\ud5a5",
          "plcDist": "\uacf5\uacf5\uac74\ubb3c(\uc7a5\uc18c) \uac70\ub9ac",
          "parkQty": "\uc8fc\ucc28 \uac00\ub2a5\ub300\uc218",
          "parkXpnsYn": "\uc8fc\ucc28\uc7a5 \uc6b4\uc601\uc5ec\ubd80, \uc8fc\ucc28\ube44\uc6a9 \ubd80\ub2f4\uc5ec\ubd80",
          "parkEtc": "\uae30\ud0c0 \uc548\ub0b4\uc0ac\ud56d",
          "noTrmtSun": "\uc77c\uc694\uc77c \ud734\uc9c4 \uc548\ub0b4",
          "noTrmtHoli": "\uacf5\ud734\uc77c \ud734\uc9c4 \uc548\ub0b4",
          "emyDayYn": "\uc8fc\uac04 \uc751\uae09\uc2e4 \uc6b4\uc601\uc5ec\ubd80",
          "emyDayTelNo1": "\uc8fc\uac04 \uc751\uae09\uc2e4 \uc804\ud654\ubc88\ud638 1",
          "emyDayTelNo2": "\uc8fc\uac04 \uc751\uae09\uc2e4 \uc804\ud654\ubc88\ud638 2",
          "emyNgtYn": "\uc57c\uac04 \uc751\uae09\uc2e4 \uc6b4\uc601\uc5ec\ubd80",
          "emyNgtTelNo1": "emyNgtTelNo1\t\uc57c\uac04 \uc751\uae09\uc2e4 \uc804\ud654\ubc88\ud638 1",
          "emyNgtTelNo2": "emyNgtTelNo1\t\uc57c\uac04 \uc751\uae09\uc2e4 \uc804\ud654\ubc88\ud638 2",
          "lunchWeek": "\uc6d4~\uae08 \uc810\uc2ec\uc2dc\uac04"
        },
        "getFacilityInfo": {
            "yadmNm": "병원명",
            "clCd": "종별 코드",
            "clCdNm": "종별 코드명",
            "orgTyCd": "설립 구분",
            "orgTyCdNm": "설립 구분명",
            "sidoCd": "시도코드",
            "sidoCdNm": "시도명",
            "sgguCd": "시군구코드",
            "sgguCdNm": "시군구명",
            "emdongNm": "읍면동명",
            "postNo": "우편번호",
            "addr": "주소",
            "telno": "전화번호",
            "hghrSickbdCnt": "상급 입원실(병상수)",
            "stdSickbdCnt": "일반 입원실(병상수)",
            "aduChldSprmCnt": "성인/소아 중환자실(병상수)",
            "nbySprmCnt": "신생아 중환자실(병상수)",
            "partumCnt": "분만실(병상수)",
            "soprmCnt": "수술실(병상수)",
            "emymCnt": "응급실(병상수)",
            "ptrmCnt": "물리치료실(병상수)",
            "hospUrl": "홈페이지",
            "estbDd": "개설일자"
        },
        "getNonPaymentItemHospList": {
            "clCd": "종별코드(병원구분코드)",
            "clCdNm": "종별코드명(병원구분)",
            "divCd1": "1차분류코드(항목명코드)",
            "divCd1Nm": "1차분류코드명(항목명)",
            "divCd2": "2차분류코드(중분류코드)",
            "divCd2Nm": "2차분류코드명(중분류)",
            "divCd3": "3차분류코드",
            "divCd3Nm": "3차분류코드명",
            "invtDt": "기준일",
            "itmCd": "항목코드",
            "itmCdNm": "항목코드명(병원사용명칭)",
            "itmPrcMax": "항목의 최대비용",
            "itmPrcMin": "항목의 최소비용",
            "prcMax": "최대비용",
            "prcMin": "최소비용",
            "rmk1": "비고1",
            "sgguCd": "시군구코드",
            "sgguCdNm": "시군구명",
            "sidoCd": "시도코드",
            "sidoCdNm": "시도명",
            "url": "확인URL",
            "yadmNm": "병원명",
            "ykiho": "암호화된 요양기호"
        },
        "getNonPaymentItemCodeList" : {
            "divCd1": "1차분류코드",
            "divCd1Nm": "1차분류코드명",
            "divCd1Dsc": "1차분류코드설명",
            "divCd2": "2차분류코드",
            "divCd2Nm": "2차분류코드명",
            "divCd2Dsc": "2차분류코드설명",
            "divCd3": "3차분류코드",
            "divCd3Nm": "3차분류코드명",
            "divCd3Dsc": "3차분류코드설명"
        },
         "getPaymentNonPaymentList": {
            "impEntpNm": "수입업체명",
            "itmNm": "품목명",
            "ldgrpCd": "대분류군코드",
            "ldgrpCdNm": "대분류군코드명",
            "ldivCd": "대분류코드",
            "ldivCdNm": "대분류코드명",
            "mcatCd": "재료대코드",
            "mdivCdNm": "중분류코드명",
            "mnfEntpNm": "제조업체명",
            "mxUnprc": "상한단가",
            "nomNm": "규격명",
            "payTpNm": "급여구분명",
            "unit": "단위"
        },
        "getClinicTop5List" : {
            "crtrYm": "기준년월",
            "mfrnIntrsIlnsNm1": "국민관심질병명1",
            "mfrnIntrsIlnsNm2": "국민관심질병명2",
            "mfrnIntrsIlnsNm3": "국민관심질병명3",
            "mfrnIntrsIlnsNm4": "국민관심질병명4",
            "mfrnIntrsIlnsNm5": "국민관심질병명5",
            "shwSbjtNm": "표시과목명",
            "yadmNm": "요양기관명",
            "ykiho": "암호화된 요양기호"
        }


}

