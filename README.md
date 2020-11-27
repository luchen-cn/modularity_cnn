<script async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>
<script type="text/x-mathjax-config">
 MathJax.Hub.Config({
 tex2jax: {
 inlineMath: [["\\(","\\)"] ],
 displayMath: [ ['$$','$$'], ["\\[","\\]"] ]
 }
 });
</script>

# modularity_cnn
Calculating Modularity of CNN



Since a CNN is too large to compute network modularity, we extract a weighted undirected graph from a CNN for the calculation.
We regard nodes and edges as channels and filters in the CNN, respectively. For simplicity, pooling layers, the fully connected layer and the softmax layer are ignored. As a result, the resulting graph is with full connections between each layer with no direction. A_{ij} is calculated based on the variance in the filter v_{ij} involved with channels i and j with restoring the generalization performed by the Glorot uniform initializer.

> python3 calc_cnn_modularity.py 'hogehoge.h5'

For more details, pleace see below.
Chen, L., Murata, M. Enhancing network modularity to mitigate catastrophic forgetting. Appl Netw Sci 5, 94 (2020). https://doi.org/10.1007/s41109-020-00332-9

