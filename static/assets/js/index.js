$(document).ready(function () {
			$('#list').on('click', function () {
				$('#products .item').addClass('list-group-item');
			});
			$('#grid').on('click', function () {	
				$('#products .item').removeClass('list-group-item');
				$('#products .item').addClass('grid-group-item');
			});
			
			$('.comic_item').on('click', function () {	
				console.log($(this).attr('api_url'));
				window.location.replace(window.location.origin + '/comic_info/' + $(this).attr('api_url'));
			});
        });