***멋쟁이사자처럼 2주차 세션***

*1. View 연결*

- view : 사용자에게 요청을 받아 데이터를 처리, 반환하는 역할

    > -> 사용자가 URL 요청, 요청을 처리할 View 함수 호출
    > -> 로직 수행, DB 처리 등 작업 수행
    > -> 처리한 데이터를 template에 전달
    > -> 사용자에게 웹 페이지 응답

- views.py, urls.py를 이용해 반드시 url과 url에 해당하는 데이터와 연결해야 함
    > -> views.py작성, urls.py 작성, html페이지와 view 연결

*2. Templates*
- Templates : 사용자에게 보여지는 웹 페이지의 뼈대, 구조

    > -> Template은 HTML과 Django 템플릿 언어로 구성됨.
    > -> 사용자가 페이지를 요청했을 때 서버의 데이터와 템플릿을 조합하여 완성된 HTML을 보여줌

- main 폴더 안에 Template 폴더를 안에 html 파일을 만들어 사용

- template 언어 : 파이썬의 문법을 html에서 사용할 수 있도록 함.
    > -> 크게 템플릿 변수, 템플릿 태그, 템플릿 필터, 템플릿 주석 4가지 기능을 지원.

- 템플릿 변수 : 뷰에서 전달한 데이터를 '{{ }}' 형태를 이용하여 웹 페이지에 출력
    > -> 변수 : {{ 변수명 }}
         ex) {{ generation }}

    > -> 변수의 속성 : {{ 변수명.속성명 }}
        ex) {{ info.weather }}, {{ info.feeling }}

    > -> list의 Index 값 : {{ list명.list순서 }}
        ex) {{ arr.1 }}

    > -> dict의 Key 값 : {{ dict.key }}
        ex) {{ dict.name }}, {{ dict.age }}

- 템플릿 태그 : for문, if문 등의 파이썬 문법을 html 내에서 사용 가능

    > 조건문 : {% if 조건 %}, {% else %}, {% endif %} 구조로 사용

    > 반복문 : {% for i in num %}, {{ num }}, {% endfor %} 구조로 사용

- 템플릿 필터 : {{ 변수 | 필터 }} 형태로 사용하며 데이터 가공, 포맷 변경에 사용됨
    ex) {{ arr|length }} : 문자열 길이 반환
        {{ name|lower }}/{{ name|upper }} : 문자열 소문자 / 대문자 변환
        {{ today|date }} : 날짜 포맷 지정 등

- 템플릿 주석 : 서버 렌더링 과정에서 완전히 무시되고 클라이언트에도 보이지 않는 주석
    > -> {# 템플릿 주석 내용 #} 형태로 사용. 코드 설명, 디버깅 시 유용하게 사용.


*3. Template 상속*

- Template 상속 : 공통 레이아웃을 정의하는 기반 템플릿.

    > -> 공통적으로 사용되는 부분을 한 군데에 묶고, 개별 내용만 필요한 곳에 작성하여 코드 작성 효율을 높임

    > -> 코드 재사용, 유지 보수, 가독성 등의 장점이 있음

    > -> Navbar, footer 등 많은 페이지에서 반복적으로 사용되는 부분을 Template 상속을 이용하여 사용.


- 주요 문법

    > -> {% extends "파일명" %} : 상속받을 기반 템플릿 선언

    > -> {% block 블록명 %} : 상속받은 템플릿에 정의된 블록 영역 선언

    > -> {% endblock %} : block 끝 표시


- 유의할 점

    > -> 반드시 project/settings.py에서 os를 import하고, 템플릿 파일의 경로를 설정해야 함.


*4. Static*

- Static : 정적 파일. 이미지, css등 이미 존재하는 파일을 그대로 클라이언트에 전달해주는 정적 리소스.

- project/static 폴더 내에 css, images 등의 폴더를 만들어 사용.

- {% load static %}
    <img src='{% static 파일명 %}' alt="" width=""> : 이미지 활용
    <link rel="" type="text/css" href="{% static 'css파일 경로' %}"> : css파일 활용

- settings.py에서 os.path.join 형태로 활용 경로를 설정해주어야 함.