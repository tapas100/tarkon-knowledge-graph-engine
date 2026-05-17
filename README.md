# tarkon-knowledge-graph-engine

The **Knowledge Graph Engine** maintains a dynamic, curriculum-aligned knowledge graph that maps concepts, their relationships, prerequisites, and each student's mastery level.

---

## Responsibilities

- Build and maintain a curriculum knowledge graph (concepts + relationships)
- Track per-student concept mastery (0–1 mastery score)
- Compute prerequisite chains and learning paths
- Identify knowledge gaps from assessment data
- Serve graph data for visualisation in student and teacher UIs
- Feed concept data to `tarkon-weakness-detection-engine` and `tarkon-assignment-engine`
- Support subject-specific sub-graphs (Maths, Science, English, etc.)

---

## Tech Stack

| Layer        | Technology                         |
|--------------|------------------------------------|
| Language     | Python 3.12                        |
| Framework    | FastAPI                            |
| Graph DB     | Neo4j                              |
| Driver       | neo4j Python driver                |
| Algorithms   | NetworkX (path finding, centrality)|
| Testing      | pytest                             |

---

## Project Structure

```
src/
  __init__.py
  api.py
  config.py
  graph/
    __init__.py
    neo4j_client.py
    builder.py
    traversal.py
    learning_path.py
    mastery_updater.py
  models/
    __init__.py
    concept.py
    relationship.py
    mastery.py
    learning_path.py
  services/
    __init__.py
    graph_service.py
    mastery_service.py
    path_service.py
  utils/
    __init__.py
    cypher.py
config/
  graph_schema.yaml
  subjects/
    mathematics.yaml
    science.yaml
    english.yaml
tests/
  test_traversal.py
  test_mastery.py
  test_learning_path.py
docs/
Dockerfile
podman-compose.yml    # includes Neo4j
```

---

## API

| Method | Path                             | Description                             |
|--------|----------------------------------|-----------------------------------------|
| GET    | `/concepts`                      | List all concepts                       |
| GET    | `/concepts/{id}`                 | Get concept detail and relationships    |
| GET    | `/path`                          | Get learning path from A to B           |
| GET    | `/students/{id}/mastery`         | Get student's mastery across concepts   |
| POST   | `/students/{id}/mastery`         | Update mastery after assessment         |
| GET    | `/health`                        | Health check                            |

---

## Quick Start

```bash
podman-compose up -d   # starts Neo4j
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn src.api:app --reload --port 9009
```

---

## License

MIT
