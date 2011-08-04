from django.conf.urls.defaults import *

urlpatterns = patterns('',
                       (r'^login/$', 
                        'django.contrib.auth.views.login', 
                        {'template_name': 'accounts/login.html'}),

			(r'^profile/$','The_Xaming_Arena.exam.views.profile',
			{'template_name':'accounts/profile.html'}),

		       (r'^home/$', 'The_Xaming_Arena.exam.views.home',
			{'template_name': 'accounts/home.html'}),

			(r'^questions/$','The_Xaming_Arena.exam.views.topics',
			{'template_name':'accounts/topics.html'}),

			(r'questions/(?P<sub_code>[^/]+)/view_questions/$','The_Xaming_Arena.exam.views.view_questions',
			{'template_name':'accounts/view_questions.html'}),

			(r'^sub_report/$','The_Xaming_Arena.exam.views.sub_rep',
			{'template_name':'accounts/sub_res.html'}),

			(r'questions/(?P<sub_code>[^/]+)/reports/$','The_Xaming_Arena.exam.views.reports',
			{'template_name':'accounts/reports.html'}),

                       (r'^logout/$', 
                        'django.contrib.auth.views.logout', 
                        {'template_name': 'accounts/logged_out.html'}),

			(r'^exam/$', 'The_Xaming_Arena.exam.views.select_topic',
			{'template_name':'accounts/select_topic.html'}),

			(r'^exam/(?P<sub_code>[^/]+)/start_exam/$','The_Xaming_Arena.exam.views.start_exam',
			{'template_name':'accounts/start_exam.html'}),

                       (r'^password_change/$', 
                        'django.contrib.auth.views.password_change', 
                        {'template_name': 'accounts/password_change_form.html'}),

                       (r'^password_change/done/$', 
                        'django.contrib.auth.views.password_change_done', 
                        {'template_name': 'accounts/password_change_done.html'}),

  )
