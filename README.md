# M3  
Этот проект создан для понимания работы пакета M3 core в связке с Objectpack.  

## Задача  

В данном проекте была задача реализовать GUI интерфейс CRUD операций для моделей:  
  1. ContentType  
  2. User  
  3. Group  
  4. Permission  
Для модели User, реализовать окно редактирования и добавления записи ручным способом, описанным в https://objectpack.readthedocs.io/ru/latest/tutorial.html#id8,  
не фабричным способом(не использовать конструкцию 
`add_window = edit_window = objectpack.ui.ModelEditWindow.fabricate(model)`).  
При этом, в данном окне должны присутствовать все поля, которые бы присутствовали при создании фабричным способом.  
(Как вариант -- можно сначала создать окно фабричным способом, посмотреть, какие поля представлены в окне, после чего написать собственное окно, представляющее те же поля).

## Установка необходимых пакетов  
Как оказалось, эти пакеты работают корректно только с определенными версиями библиотек, которые, в большинстве своем, уже устарели.  

### Способ № 1. Установка с помощью файла зависимостей requirements.txt  

Для установки необходимых пакетов в автоматическом режиме можно воспользоваться файлом requirements.txt. У меня он находится на одном уровне с папкой виртуального окружения.  
Внутри него указаны пакеты и их версии, необходимые вам для работы в формате **<название пакета>==<версия>** (без скобок).
Выше указаны ресурсы, с которых требуется эти пакеты скачать. 
После кода `--extra-index-url` указан дополнительный индекс, с которого необходимо скачать пакет при отсутствии данного пакета по основному индексу.  
После кода `--trusted-host` указан доверенный хост, что бы это ни значило.
Таким образом мой файл выглядит так:  
```
    --extra-index-url http://pypi.bars-open.ru/simple/  
    --trusted-host pypi.bars-open.ru  
  
    django==2.2.2  
    m3-django-compat==1.9.2  
    m3-objectpack==2.2.47  
```
Теперь в командной строке пишем `pip install -r requirements.txt` и ждем когда пакеты установятся.

### Способ № 2. Установка вручную  
Бывает, что в автоматическом режиме установка не происходит по разным причинам. Так же произошло и у меня. Решил проблему с помощью установки пакетов вручную.
    
#### Python  

Требуется Python версии 3.6. Здесь ничего сложного, устанавливаем как обычно, просто версия иная.

#### Django  

Фреймворк Django нужен версии 2.2.2. Так же ничего сложного. в терминале пишем `pip install django2.2.2`.

#### M3-django-compat

Здесь ***pip*** может не найти требуемую версию. Устанавливаем следующим образом:
  1. Скачиваем требуемый пакет с сайта `https://pypi.bars-open.ru/simple/`. 
  2. В терминале пишем `pip install -e <path>`. Вместо ***<path>*** нужно указать абсолютный путь до файла setup.py, либо до папки, в которой содержится этот файл.  

#### M3-objectpack
  С этим пакетом аналогично как и с m3-django-compat.  
  
P.S. Сразу отмечу, что для корректной работы данных пакетов в связке лучше использовать именно версии, указанные в вышеупомянутом файле requirements.txt и с python 3.6.  
  
## Подключение рабочего стола m3  
  
  1. Развернуть django-проект m3_project и создать django-приложение app.  
  2. Подключить рабочий стол m3:  
      I. Внутри приложения app на одном уровне с файлами admin.py, models.py и др. созданными автоматически, дополнительно вручную создать файлы:  
  
          1. actions.py  
          2. app_meta.py  
          3. context_processors.py  
          4. controller.py  
          5. ui.py  
  
      II. Создать контроллер приложения в файле controller.py:  
  
          from objectpack.observer import (
              ObservableController,
              Observer,
              )
  
          observer = Observer()
          controller = ObservableController(
              url='actions', 
              observer=observer,
              )
  

      III. Зарегистрировать контроллер и элементы рабочего стола и экшн-паки в файле app_meta.py:  
  

          from django.conf.urls import url  
          from objectpack import desktop  
          from .controller import controller  


          def register_urlpatterns():  
            """  
            Регистрация конфигурации урлов для приложения  
            """  
            return [url(*controller.urlpattern)]  


          def register_actions():  
            """  
            Регистрация экшен-паков  
            """  
            return controller.packs.extend([  
                    # YourActionPack()  
            ])  

          def register_desktop_menu():  
            """  
            регистрация элементов рабочего стола  
            """  
            desktop.uificate_the_controller(  
                    controller,  
                    menu_root=desktop.MainMenu.SubMenu('Demo')  
            )  

      IV. Создание обработчика контекста в файле context_processors.py:  
        
          from m3_ext.context_processors import DesktopProcessor

          def desktop(request):  
            return DesktopProcessor.process(request)
      V. Модифицировать settings.py:  
  
          INSTALLED_APPS = [  
            # ...  
            'app',  
            'm3_ext',  
            'm3_ext.ui',  
            'objectpack',  
            ]  
      VI. Добавить созданный обработчик контекста:  
  
          TEMPLATES = [  
              {
                # ...  
                'OPTIONS': {
                  'context_processors': [
                    # ...
                    'app.context_processors.desktop',
                  ],
                },
              },
          ]  
      VII. Закомментировать строку 'django.middleware.csrf.CsrfViewMiddleware', в MIDDLEWARE  
      VIII. Подключить рабочий стол m3 в urls.py:  
          
          from django.conf import settings  
          from django.conf.urls import url  
          from django.contrib import admin  
          from django.shortcuts import render  
  
          from m3 import get_app_urlpatterns  
  
  
          def workspace(request):  
            """  
            Возвращает view для отображения Рабочего Стола на  
            основе шаблона m3  
            """  
            return render(  
                    request,  
                    'm3_workspace.html',  
                    context={'debug': settings.DEBUG},  
            )  
  
  
          urlpatterns = [  
            url(r'^admin/', admin.site.urls),  
            url(r'^$', workspace),  
          ]  
  
          # Собираем шаблоны урлов из app_meta  
          # подключенных приложений  
          urlpatterns.extend(get_app_urlpatterns())  
  Если все работает верно, то при запущенном сервере должно получиться следующее:  
  
  ![То, что должно получиться](https://github.com/RomanKim94/M3/assets/126502451/ea558b0f-56a9-4181-8fd9-f32a5d52b7e1)  
  
  ## Ссылки на документацию  
  
    - m3-core: https://m3-core.readthedocs.io/ru/latest/  
    - objectpack: https://objectpack.readthedocs.io/ru/latest/
