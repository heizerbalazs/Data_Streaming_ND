# How did changing values on the SparkSession property parameters affect the throughput and latency of the data?

I measured the performance based on inputRowsPerSecond and processedRowsPerSecond.
throughput = processedRowsPerSecond [1/s]
latency = (1/processedRowsPerSecond-1/inputRowsPerSecond)*1000 [ms]

# What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?

