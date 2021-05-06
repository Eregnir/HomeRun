"use strict"; 
var routes = [
  // Index page
  {
    path: '/',
    url: '/',
    name: 'home',
  },
  // Home V2
  {
    path: '/home_2',
    url: '/home_2',
    name: 'home_2',
  },
  // Cart
  {
    path: '/cart/',
    url: '/cart',
    name: 'cart',
  },
  // Books List
  {
    path: '/books_list/',
    url: '/books_list',
    name: 'books_list',
	on: {
		pageInit: function() {
			$$('.display-style').on('click' ,'a', function(){
				if($$(this).hasClass('display-style-active')) {
					return;
				} else {
					$$('.display-style').find('.display-style-active').removeClass('display-style-active');
					$$(this).addClass('display-style-active');
					var style = $$(this).attr('data-display');
					console.log(style);
					if(style == "list") {
						var p = $$(this).parent().parent().parent().find('.books-grid');
						p.addClass('books-list').removeClass('books-grid books-grid-two-colums row');
						p.find('.book-description').css('display', 'block');
						p.find('.book-grid').addClass('book-list').removeClass('book-grid').addClass('display-flex');
						
					} else if(style == "grid") {
						var p = $$(this).parent().parent().parent().find('.books-list');
						p.addClass('books-grid books-grid-two-colums row').removeClass('books-list');
						p.find('.book-description').css('display', 'none');
						p.find('.book-list').addClass('book-grid').removeClass('book-list').removeClass('display-flex');
					}
				}
				return false;
			});
		}
	}
  },
  // Free book Single
  {
    path: '/free_book_single/',
    url: './pages/free_book_single.html',
    name: 'free_book_single',
  },
  // Paid book Single
  {
    path: '/paid_book_single/',
    url: './pages/paid_book_single.html',
    name: 'paid_book_single',
  },
  // BookShelf
  {
    path: '/bookshelf/',
    url: '/bookshelf',
    name: 'bookshelf',
  },
  // Profile
  {
    path: '/profile/',
    url: '/profile',
    name: 'profile',
  },
  // Pages
  {
    path: '/pages/',
    url: '/pages',
    name: 'pages',
  },
  // Reading
  {
    path: '/reading/',
    url: '/reading',
    name: 'reading',
	on: {
		pageInit: function() {
			$$('#font-size').on('range:change', function (e, range) {
				$$(".reading-text").css("font-size",range.value+"px");
			});
			
			$$(".page-colors a").click(function(){
				if($$(this).hasClass('active')) {
					$$(this).removeClass('active');
				} else {
					$$(".page-colors").find('a').removeClass('active');
					$$(this).addClass('active');
				}
				
			});
		}
	}
  },
  // Cover
  {
    path: '/cover/',
    url: '/cover',
    name: 'cover',
  },
  // Default route (404 page). MUST BE THE LAST
  {
    path: '(.*)',
    url: './pages/404.html',
  },
];
