$("#sender").click(function () {
    var input = $('#user-input').val();
    alert(input);

    $.ajax({
        url: '/get_response/',
        data: {
          'inputValue': input
        },
        dataType: 'json',
        success: function (data) {
          document.getElementById('p-text').innerHTML = data["respond"];
        }
      });
    });