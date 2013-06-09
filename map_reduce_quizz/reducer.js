// Reducer() : key is a made hand, e.g. 'flush' .
// Count up how many unique hands make e.g. a flush.
function Reducer(jsmr_context, key) {
  var sum = 0;
  while (jsmr_context.HaveMoreValues()) {
    var count_str = jsmr_context.GetNextValue();
    sum += parseInt(count_str);
  }
  jsmr_context.Emit(key + ':' + sum.toString());
}
