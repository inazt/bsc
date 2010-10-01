(function($) {

  $.build = {
    
    init: function() {

      var $news = $('#latest_news .scrollable').scrollable({
      });

      $news_api = $news.data('scrollable');

      $news_api.onSeek(function(e, i) {

        if (i < $news_api.getSize()) {
          $('.more', $news).show();
        }

      });

      // Navigation.
      $('.next').click(function(event) {

        event.preventDefault();

        $.getJSON('/json/news/get', {page: $news_api.getIndex() + 1}, function(result) {

          var $itemWrapper = $('<div></div>');
          for(i in result) {
            var $item = $('<div></div>').addClass('item').appendTo($itemWrapper);
            $('<h2></h2>').html('News').appendTo($item);
            $('<img />').attr({
              src: 'http://www.lipsum.com/images/lipsum05.gif',
              width: 162,
              height: 130
            }).appendTo($item);
            var $title = $('<div></div>').addClass('title');
            $('<a></a>').attr('href', '#').html(result[i].fields.title).appendTo($title);
            $title.appendTo($item);
            $('<div></div>').addClass('description').html(result[i].fields.body).appendTo($item);
          }

          $news_api.addItem($itemWrapper).end();

        });

      });
    },

    addNewsItems: function(items) {

    }

  }

  $(document).ready(function() {

    $.build.init();

  });

})(jQuery);
