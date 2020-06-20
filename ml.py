from markovclick.models import MarkovClickstream
m = MarkovClickstream(data)
fig=plt.figure(figsize=(18, 16), dpi= 80, facecolor='w', edgecolor='k')
sns.heatmap(m.prob_matrix, xticklabels=m.pages, yticklabels=m.pages,cmap="YlGnBu")
from markovclick.viz import visualise_markov_chain
graph = visualise_markov_chain(m)
graph