"""BERTopic class to interact with the corresponding package."""

from pathlib import Path
from typing import Any, Optional

import pandas as pd
import plotly.graph_objects as go

from tripadvisor_hotel_reviews_topic_modeling.utils.file_handler import load_object

DATA_DIR = Path(__file__).parents[2].joinpath("data")


class BERTopicLabel:
    """Interact with Google BigQuery."""

    def __init__(
        self,
        label: str,
        data: pd.DataFrame,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        """Initialises the BERTopicLabel class.

        Args:
            label (str): a label that could be found in the data BERTopic was fitted on.
            data (pd.DataFrame): the pandas DataFrame BERTopic was fitted on.

        """
        # Set the BERTopic attributes.
        self.data = data
        self.label = label
        self.review_label = self.data.loc[
            self.data["label"] == self.label, "review"
        ].reset_index(drop=True)

        self.model = load_object(f"{DATA_DIR}/topic_model_{self.label}.pkl")
        self.topics = load_object(f"{DATA_DIR}/topics_label_{self.label}.pkl")
        self.probs = load_object(f"{DATA_DIR}/probs_label_{self.label}.pkl")

        self.topic_info = self.model.get_topic_info()
        self.nb_topic = self.topic_info.shape[0]

    def get_number_topic(self) -> str:
        """Get the number of topics found.

        Returns:
            str: a string with insights on the number of topics and reviews.

        """
        total_nb_reviews = len(self.review_label)

        return f"""The total number of topics for the {self.label} reviews is
        {self.nb_topic} for a total number of {total_nb_reviews} reviews."""

    def get_topn_topic_info(self, n_topic: int) -> pd.DataFrame:
        """Get word information from the top n topics in terms of count.

        Args:
            n_topic (int): the number of topics to get information on.

        Returns:
            pd.DataFrame: a pandas DataFrame containing information on
            the n top topics.

        """
        return self.topic_info.head(n_topic)

    def get_dendrogram(self) -> go.Figure:
        """Get dendrogam from a fitted BERTopic instance.

        Returns:
            go.Figure: a plotly figure representing the dendrogram
            of the fitted BERTopic instance.

        """
        return self.model.visualize_hierarchy(top_n_topics=self.nb_topic)

    def reduce_topic_number(self, n_topic: int) -> None:
        """Reduce number of topics to `n_topic`.

        Args:
            n_topic (int): the expected number of topics.

        """
        _, _ = self.model.reduce_topics(
            self.review_label, self.topics, self.probs, nr_topics=n_topic
        )

    def get_barchart_top5words_by_topic(
        self, n_topic: Optional[int] = None
    ) -> go.Figure:
        """Get importance of the top 5 words for each top n topic.

        Args:
            n_topic (Optional[int]): the number of topics to get
            the barcharts on.

        Returns:
            go.Figure: a plotly figure with barchats for the top 5
            words for each topo n topic.

        """
        if n_topic is None:
            n_topic = self.nb_topic
        return self.model.visualize_barchart(top_n_topics=n_topic)

    def get_topic_review(self) -> pd.DataFrame:
        """Get the topic for each review.

        Returns:
            pd.DataFrame: a pandas DataFrame containing the reviews
            and their associated topic.

        """
        topic, _ = self.model.transform(self.review_label)
        reviews_predicted_topic = pd.DataFrame(
            {"review": self.review_label, "topic": topic}
        )
        return reviews_predicted_topic

    def get_sample_reviews_for_topic(
        self, topic_review_df: pd.DataFrame, topic_nb: int, nb_reviews: int
    ) -> None:
        """Get a sample of reviews for a specific topic.

        Args:
            topic_review_df (pd.DataFrane): a pandas DataFrame
            containing reviews and their associated topic number.
            topic_nb (int): a topic number.
            nb_reviews (int): the number of samples to get.

        """
        print(
            topic_review_df.loc[topic_review_df["topic"] == topic_nb, "review"]
            .sample(n=nb_reviews, random_state=42)
            .str.cat(sep="\n\n")
        )
