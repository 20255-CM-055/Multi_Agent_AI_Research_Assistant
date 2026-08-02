from dataclasses import dataclass


@dataclass
class Document:
    """
    Represents a piece of information retrieved
    from any knowledge source.
    """

    title: str

    url: str

    content: str

    source: str