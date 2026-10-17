---
id: study_0088
title: "JSON-LD"
rank: 95
views: 795679
url: "https://en.wikipedia.org/wiki/JSON-LD"
pageid: 34228206
description: "File format for encoding linked data"
summary: "JSON-LD (JavaScript Object Notation for Linked Data) is a method of encoding linked data using JSON and of serializing data similarly to traditional JSON. It is meant to be simple to create by modifying JSON documents. JSON-LD is a World Wide Web Consortium Recommendation initially developed by the JSON for Linking Data Community Group, transferred to the RDF Working Group for review, improvement and standardization, and now maintained by the JSON-LD Working Group."
source: Wikipedia
license: "CC BY-SA 4.0"
month: "2026-09"
retrieved: 2026-10-16
---

# JSON-LD

**JSON-LD** (**JavaScript Object Notation for Linked Data**) is a method of encoding [linked data](https://en.wikipedia.org/wiki/Linked_data "Linked data") using [JSON](https://en.wikipedia.org/wiki/JSON "JSON") and of serializing data similarly to traditional JSON. It is meant to be simple to create by modifying JSON documents. JSON-LD is a [World Wide Web Consortium Recommendation](https://en.wikipedia.org/wiki/World_Wide_Web_Consortium#W3C_recommendation_(REC) "World Wide Web Consortium") initially developed by the JSON for Linking Data Community Group, transferred to the RDF Working Group for review, improvement and standardization, and now maintained by the JSON-LD Working Group.

## Design

JSON-LD is based on the concept of a "context" that maps JSON object properties to concepts in an [ontology](https://en.wikipedia.org/wiki/Ontology_(information_science) "Ontology (information science)") using an [RDF](https://en.wikipedia.org/wiki/Resource_Description_Framework "Resource Description Framework") model. In order to map the JSON-LD syntax to RDF, JSON-LD allows values to be coerced to a specified type or tagged with a language. A context can be embedded directly in a JSON-LD document or put into a separate file and referenced from traditional JSON documents via an [HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol "Hypertext Transfer Protocol") Link [header](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields "List of HTTP header fields").

## Example

```
{
  "@context": {
    "name": "http://xmlns.com/foaf/0.1/name",
    "homepage": {
      "@id": "http://xmlns.com/foaf/0.1/workplaceHomepage",
      "@type": "@id"
    },
    "Person": "http://xmlns.com/foaf/0.1/Person"
  },
  "@id": "https://me.example.com",
  "@type": "Person",
  "name": "John Smith",
  "homepage": "https://www.example.com/"
}
```

The example above describes a person, based on the [FOAF (friend of a friend) ontology](https://en.wikipedia.org/wiki/FOAF_(ontology) "FOAF (ontology)"). First, the two JSON properties `name` and `homepage` and the type `Person` are mapped to concepts in the FOAF vocabulary and the value of the `homepage` property is specified to be of the type `@id`. In other words, the homepage id is specified to be an [IRI](https://en.wikipedia.org/wiki/Internationalized_Resource_Identifier "Internationalized Resource Identifier") in the context definition. Based on the RDF model, this allows the person described in the document to be unambiguously identified by an [IRI](https://en.wikipedia.org/wiki/Internationalized_Resource_Identifier "Internationalized Resource Identifier"). The use of resolvable IRIs allows RDF documents containing more information to be [transcluded](https://en.wikipedia.org/wiki/Transclusion "Transclusion") which enables clients to discover new data by following those links; this principle is known as 'Follow Your Nose'.

By having all data semantically annotated as in the example, an RDF processor can identify that the document contains information about a person (`@type`) and if the processor understands the FOAF vocabulary it can determine which properties specify the person's name and homepage.

## Use

The encoding is used by [Schema.org](https://en.wikipedia.org/wiki/Schema.org "Schema.org"), [Google Knowledge Graph](https://en.wikipedia.org/wiki/Google_Knowledge_Graph "Google Knowledge Graph"), and used mostly for [search engine optimization](https://en.wikipedia.org/wiki/Search_engine_optimization "Search engine optimization") activities. It has also been used for applications such as [biomedical informatics](https://en.wikipedia.org/wiki/Health_informatics "Health informatics"), and representing [provenance](https://en.wikipedia.org/wiki/Provenance "Provenance") information. It is also the basis of [Activity Streams](https://en.wikipedia.org/wiki/Activity_Streams_(format) "Activity Streams (format)"), a format for "the exchange of information about potential and completed activities", and is used in [ActivityPub](https://en.wikipedia.org/wiki/ActivityPub "ActivityPub"), the federated social networking protocol. Additionally, it is used in the context of [Internet of Things (IoT)](https://en.wikipedia.org/wiki/Internet_of_things "Internet of things"), where a Thing Description, which is a JSON-LD document, describes the network facing interfaces of IoT devices.

---

*Source: [Wikipedia — JSON-LD](https://en.wikipedia.org/wiki/JSON-LD). Text licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*
