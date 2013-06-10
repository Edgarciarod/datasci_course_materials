// Kernel() : Generate all 5-card poker hands as csv string. 
// e.g. : '3S,QC,AD,AC,7H'  (5 cards in each emitted data line) 
function Kernel(jsmr_context) {
    var faces = [
        '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'
    ];
    var suits = [ 'S', 'C', 'D', 'H' ];  // Spades, Clubs, Diamonds, Hearts

    var all_cards = [];
    for (var f = 0; f < faces.length; f++) {
        for (var s = 0; s < suits.length; s++) {
            var card = faces[f] + suits[s];  // construct e.g. 'QH' for Q of Hearts
            all_cards.push(card);
        }
    }

    // generate all unique 5-card combinations (poker hands)
    var all_cards_len = all_cards.length;  // cache for perf
    for (var i1 = 0; i1 < all_cards_len; i1++) {
        for (var i2 = i1 + 1; i2 < all_cards_len; i2++) {
            for (var i3 = i2 + 1; i3 < all_cards_len; i3++) {
                for (var i4 = i3 + 1; i4 < all_cards_len; i4++) {
                    for (var i5 = i4 + 1; i5 < all_cards_len; i5++) {
                        var hand = all_cards[i1] + ',' +
                            all_cards[i2] + ',' +
                            all_cards[i3] + ',' +
                            all_cards[i4] + ',' +
                            all_cards[i5];
                        jsmr_context.Emit(hand);
                    }
                }
            }
        }
    }
}
