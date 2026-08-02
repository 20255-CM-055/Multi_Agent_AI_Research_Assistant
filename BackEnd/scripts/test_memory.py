from services.memory_service import MemoryService

memory = MemoryService()

documents = memory.search(
    "Artificial Intelligence"
)

print(f"Retrieved: {len(documents)} documents\n")

for doc in documents:
    print("=" * 60)
    print(doc.title)
    print(doc.source)
    print(doc.content[:200])