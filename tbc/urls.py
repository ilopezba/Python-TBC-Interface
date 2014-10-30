from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'tbc.views.Home', name='Home'),
    url(r'^internship-forms/$', 'tbc.views.InternshipForms', name='InternshipForms'),
    url(r'^about-pythontbc/$', 'tbc.views.AboutPytbc', name='AboutPytbc'),
    url(r'^sample-notebook/$', 'tbc.views.SampleIpynb', name='SampleIpynb'),
    url(r'^register/$', 'tbc.views.UserRegister', name='UserRegister'),
    url(r'^login/$', 'tbc.views.UserLogin', name='UserLogin'),
    url(r'^logout/$', 'tbc.views.UserLogout', name='UserLogout'),
    url(r'^profile/$', 'tbc.views.UserProfile', name='UserProfile'),
    url(r'^forgot-password/$', 'tbc.views.ForgotPassword', name='ForgotPassword'),
    url(r'^update-password/$', 'tbc.views.UpdatePassword', name='UpdatePassword'),
    
    
    url(r'^submit-proposal/$', 'tbc.views.SubmitProposal', name='SubmitProposal'),
    url(r'^submit-aicte-proposal/$', 'tbc.views.ListAICTE', name='ListAICTE'),
    url(r'^submit-aicte-proposal/(?P<aicte_book_id>\d+)/$', 'tbc.views.SubmitAICTEProposal', name='SubmitAICTEProposal'),
    url(r'^submit-book/$', 'tbc.views.SubmitBook', name='SubmitBook'),
    url(r'^submit-sample/$', 'tbc.views.SubmitSample', name='SubmitSample'),
    url(r'^submit-sample/(?P<proposal_id>\d+)$', 'tbc.views.SubmitSample', name='SubmitSample'),
    url(r'^submit-sample/(?P<proposal_id>\d+)/(?P<old_notebook_id>\d+)$', 'tbc.views.SubmitSample', name='SubmitSample'),
    url(r'^confirm-book-details/$', 'tbc.views.ConfirmBookDetails', name='ConfirmBookDetails'),
    url(r'^submit-code/$', 'tbc.views.SubmitCode', name='SubmitCode'),
    url(r'^update-content/(?P<book_id>\d+)$', 'tbc.views.UpdateContent', name='UpdateContent'),
    url(r'^get-zip/(?P<book_id>\d+)$', 'tbc.views.GetZip', name='GetZip'),
    url(r'^browse-books/$', 'tbc.views.BrowseBooks', name='BrowseBooks'),
    url(r'^browse-books/(?P<category>.+)$', 'tbc.views.BrowseBooks', name='BrowseBooks'),
    url(r'^convert-notebook/(?P<notebook_path>.+)$', 'tbc.views.ConvertNotebook', name='ConvertNotebook'),
    url(r'^book-details/(?P<book_id>\d+)/$', 'tbc.views.BookDetails', name='BookDetails'),
	url(r'^completed-books/$', 'tbc.views.CompletedBooks', name='CompletedBooks'),
	url(r'^completed-books/(?P<category>.+)$', 'tbc.views.CompletedBooks', name='CompletedBooks'),
	url(r'^books-under-progress/$', 'tbc.views.BooksUnderProgress', name='BooksUnderProgress'),
	url(r'^redirect-ipynb/(?P<notebook_path>.+)$', 'tbc.views.RedirectToIpynb', name='RedirectToIpynb'),
    
    
    url(r'^book-review/$', 'tbc.views.BookReview', name='BookReview'),
    url(r'^proposal-review/$', 'tbc.views.ReviewProposals', name='ReviewProposals'),
    url(r'^proposal-review/(?P<proposal_id>\d+)/(?P<textbook_id>\d+)$', 'tbc.views.ReviewProposals', name='ReviewProposals'),
    url(r'^disapprove-sample-notebook/(?P<proposal_id>\d+)$', 'tbc.views.DisapproveProposal', name='DisapproveProposal'),
    url(r'^allot-book/(?P<proposal_id>\d+)$', 'tbc.views.AllotBook', name='AllotBook'),
    url(r'^reject-proposal/(?P<proposal_id>\d+)$', 'tbc.views.RejectProposal', name='RejectProposal'),
    url(r'^book-review/(?P<book_id>\d+)$', 'tbc.views.BookReview', name='BookReview'),
    url(r'^approve-book/(?P<book_id>\d+)$', 'tbc.views.ApproveBook', name='ApproveBook'),
    url(r'^notify-changes/(?P<book_id>\d+)$', 'tbc.views.NotifyChanges', name='NotifyChanges'),

    # ajax urls
    url(r'^ajax/matching-books/$', 'tbc.views.ajax_matching_books', name='AjaxMatchingBooks'),

)
