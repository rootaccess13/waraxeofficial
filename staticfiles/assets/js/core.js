
  var buys = document.getElementById('buy_dias');
  paypal.Button.render({
  // Configure environment
  env: 'sandbox',
  client: {
    sandbox: 'AZnO0gKU5K3f0P1VND1U_Ur9EqerdHF41Sky-bSVS_PJieWLtlY81FdQDcAiVJYDJ6YFMvDooJOqiSsN',
    production: 'demo_production_client_id'
  },
  // Customize button (optional)
  locale: 'en_US',
  style: {
    size: 'large',
    color: 'blue',
    shape: 'pill',
  },

  // Enable Pay Now checkout flow (optional)
  commit: true,

  // Set up a payment

  payment: function(data, actions) {
    return actions.payment.create({
      transactions: [{
        amount: {
          total: buys.value,
          currency: 'USD'
        }
      }]
    });
  },
  // Execute the payment
  onAuthorize: function(data, actions) {
    return actions.payment.execute().then(function() {
      // Show a confirmation message to the buyer
      closePurchase();
      openps();

    });
  }
  }, '#paypal-button');
  function closePurchase(){
  $('#buy_diamond').each(function(){
      $(this).modal('hide');
  });
  }
  function openps(){
  $('#success_purchase').each(function(){
    $(this).modal('show');
  });
  $('#success_purchase').on('hidden.bs.modal', function () { 
      location.reload();
  });
  }


  // Load the IFrame Player API code asynchronously.
  var tag = document.createElement('script');
  tag.src = "https://www.youtube.com/player_api";
  var firstScriptTag = document.getElementsByTagName('script')[0];
  firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

  // Replace the 'ytplayer' element with an <iframe> and
  // YouTube player after the API code downloads.
  var player;
  function onYouTubePlayerAPIReady() {
    player = new YT.Player('ytplayer', {
      height: '315',
      width: '560',
      autoplay: 0,
      controls: 1, 
      rel : 0,
      fs : 0,
      videoId: 'M7lc1UVf-VE'
    });
  }
