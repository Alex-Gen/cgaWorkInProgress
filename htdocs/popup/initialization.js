$(document).ready(function() {
	$('.gruppoFoto').each(function() {
	    $(this).magnificPopup({
	        delegate: 'a[href]',
	        type: 'image',
	        tClose: 'Chiudi (Esc)',
	        gallery: {
	          enabled:true,
	          tPrev: 'Precedente (Freccia sinistra)',
  			  tNext: 'Successiva (Freccia desra)',
	          tCounter: '<span class="mfp-counter">%curr% / %total%</span>'
	        }
	    });
	});
});
