from typing import List, Tuple
from sklearn.cluster import HDBSCAN
from functional import seq
import numpy as np

def cluster(values: List[Tuple[str, List[float]]]) -> List[List[str]]:
    hdbscan = HDBSCAN(
        min_cluster_size=3,
        cluster_selection_epsilon= 1.
    )

    labels = (seq(values)
        .map(lambda x: x[0])
        .list()
    )
    embeddings = (seq(values)
        .map(lambda x: x[1])
        .map(np.array)
        .list()
    )

    clusters = hdbscan.fit(
        embeddings
    ).labels_
    
    return (seq(clusters)
        .enumerate()
        .filter(lambda x: x[1] != -1)
        .group_by(lambda x: x[1])
        .map(lambda x: seq(x[1]).map(lambda y: labels[y[0]]).list())
        .list()
    )

if __name__ == "__main__":
    from .embedding import load_model

    e = load_model()

    values = [
        "The cat sat on the mat and purred softly.",
        "A growing number of cities are adopting renewable energy sources.",
        "Artificial intelligence is transforming the healthcare industry.",
        "The stock market closed higher today, following positive economic reports.",
        "Chocolate is often used as a dessert topping or filling.",
        "Many scientists believe that climate change is accelerating.",
        "Machine learning algorithms are designed to learn patterns from data.",
        "Wildlife conservation efforts are crucial for protecting endangered species.",
        "Quantum computing promises to revolutionize complex problem-solving.",
        "Meditation and mindfulness practices can help reduce stress and anxiety.",
        "The global tech industry is seeing a surge in innovation and startups.",
        "New research suggests a possible link between diet and cognitive function.",
        "Cryptocurrencies are becoming increasingly popular as an investment option.",
        "Space exploration has expanded our understanding of the universe.",
        "The fashion industry is shifting towards more sustainable practices.",
        "Social media platforms influence the way we communicate and interact.",
        "Renewable energy technologies include solar, wind, and hydropower.",
        "Online education platforms are providing more accessible learning options.",
        "The gaming industry is rapidly evolving with advancements in virtual reality.",
        "Mobile app development is an ever-growing field with numerous opportunities."
    ]

    values = seq(values).map(e).list()
    
    print(cluster(values))

# load function
# give all values an id
# create clusters
# from map cluster back into 