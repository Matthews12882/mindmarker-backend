---
id: study_0086
title: "Microdata (HTML)"
rank: 93
views: 809639
url: "https://en.wikipedia.org/wiki/Microdata_(HTML)"
pageid: 25817778
description: "Specification for metadata in web pages"
summary: ""
source: Wikipedia
license: "CC BY-SA 4.0"
month: "2026-09"
retrieved: 2026-10-16
---

# Microdata (HTML)

**Microdata** is a part of the [WHATWG](https://en.wikipedia.org/wiki/WHATWG "WHATWG") [HTML](https://en.wikipedia.org/wiki/HTML "HTML") specification that defines how to include [metadata](https://en.wikipedia.org/wiki/Metadata "Metadata") within existing web page content. [Search engines](https://en.wikipedia.org/wiki/Search_engines "Search engines"), [web crawlers](https://en.wikipedia.org/wiki/Web_crawlers "Web crawlers"), and [browsers](https://en.wikipedia.org/wiki/Web_browser "Web browser") can extract and process Microdata from a web page and use it to provide a richer browsing experience for users. Search engines benefit greatly from direct access to Microdata because it allows them to understand the information on web pages and provide more relevant [results](https://en.wikipedia.org/wiki/Search_engine_results_page "Search engine results page") to users. Microdata uses a supporting vocabulary to describe an item and name-value pairs to assign values to its properties. Microdata is an attempt to provide a simpler way of annotating [HTML elements](https://en.wikipedia.org/wiki/HTML_element "HTML element") with machine-readable tags than the similar approaches of using [RDFa](https://en.wikipedia.org/wiki/RDFa "RDFa") and [microformats](https://en.wikipedia.org/wiki/Microformat "Microformat").

In 2013, because the W3C HTML Working Group failed to find someone to serve as an editor for the **Microdata HTML** specification, its development was terminated with a 'Note'. However, since that time, two new editors were selected, and five newer versions of the working draft have been published, the most recent being Working Draft 26 April 2018.

## Vocabularies

Microdata vocabularies do not provide the [semantics](https://en.wikipedia.org/wiki/Semantics "Semantics"), or meaning of an Item. Web developers can design a custom vocabulary or use vocabularies available on the web. A collection of commonly used markup vocabularies are provided by [Schema.org](https://en.wikipedia.org/wiki/Schema.org "Schema.org") schemas which include: *Person*, "*Place*", *Event*, *Organization*, *Product*, *Review*, *Review-aggregate*, *Breadcrumb*, *Offer*, *Offer-aggregate*. The website schema.org was established by search engine operators like [Google](https://en.wikipedia.org/wiki/Google "Google"), [Microsoft](https://en.wikipedia.org/wiki/Microsoft "Microsoft"), [Yahoo!](https://en.wikipedia.org/wiki/Yahoo! "Yahoo!"), and [Yandex](https://en.wikipedia.org/wiki/Yandex "Yandex"), which use microdata markup to improve search results.

For some purposes, an ad-hoc vocabulary is adequate. For others, a vocabulary will need to be designed. Where possible, authors are encouraged to re-use existing vocabularies, as this makes content re-use easier.

## Localization

In some cases, search engines covering specific regions may provide locally-specific extensions of microdata. For example, [Yandex](https://en.wikipedia.org/wiki/Yandex "Yandex"), a major search engine in Russia, supports [microformats](https://en.wikipedia.org/wiki/Microformats "Microformats") such as [hCard](https://en.wikipedia.org/wiki/HCard "HCard") (company contact information), [hRecipe](https://en.wikipedia.org/wiki/HRecipe "HRecipe") (food recipe), [hReview](https://en.wikipedia.org/wiki/HReview "HReview") (market reviews) and [hProduct](https://en.wikipedia.org/wiki/HProduct "HProduct") (product data) and provides its own format for definition of the terms and encyclopedic articles. This extension was made in order to solve [transliteration](https://en.wikipedia.org/wiki/Transliteration "Transliteration") problems between the [Cyrillic](https://en.wikipedia.org/wiki/Cyrillic_script "Cyrillic script") and Latin alphabets. After the implementation of additional parameters from Schema's vocabulary, indexation of information in Russian-language web-pages became more successful.

## Global attributes

* `itemscope` – Creates the Item and indicates that descendants of this [element](https://en.wikipedia.org/wiki/HTML_element "HTML element") contain information about it.
* `itemtype` – A valid URL of a vocabulary that describes the item and its properties' context.
* `itemid` – Indicates a unique identifier of the item.
* `itemprop` – Indicates that its containing tag holds the value of the specified item property. The property's name and value context are described by the item's vocabulary. Properties values usually consist of string values, but can also use URLs using the `a` element and its `href` attribute, the `img` element and its `src` attribute, or other elements that link to or embed external resources.
* `itemref` – Properties that are not descendants of the element with the `itemscope` attribute can be associated with the item using this attribute. Provides a list of element IDs (not `itemid`s) with additional properties elsewhere in the document.
* `datetime` – Indicates date or duration as specified by [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601 "ISO 8601") standard.

## Example

The following HTML5 markup may be found on a typical “About” page containing information about a person:

```
<div> Hello, my name is John Doe, I am a graduate research assistant at
the University of Dreams.
My friends call me Johnny.
You can visit my homepage at <a href="http://www.example.com/~JohnnyD">www.example.com/~JohnnyD</a>.
I live at 1234 Peach Drive, Warner Robins, Georgia.</div>
```

Here is the same markup with added [Schema.org](https://en.wikipedia.org/wiki/Schema.org "Schema.org") Microdata:

```
<div itemscope itemtype="http://schema.org/Person">
	Hello, my name is
	<span itemprop="name">John Doe</span>,
	I am a
	<span itemprop="jobTitle">graduate research assistant</span>
	at the
	<span itemprop="affiliation">University of Dreams</span>.
	My friends call me
	<span itemprop="additionalName">Johnny</span>.
	You can visit my homepage at
	<a href="http://www.example.com/~JohnnyD" itemprop="url">www.example.com/~JohnnyD</a>.
	<div itemprop="address" itemscope itemtype="http://schema.org/PostalAddress">
		I live at
		<span itemprop="streetAddress">1234 Peach Drive</span>,
		<span itemprop="addressLocality">Warner Robins</span>,
		<span itemprop="addressRegion">Georgia</span>.
	</div>
</div>
```

As the above example shows, Microdata items can be nested. In this case, an item of type <http://schema.org/PostalAddress> is nested inside an item of type <http://schema.org/Person>.

The following text shows how Google parses the Microdata from the above example code. Developers can test pages containing Microdata using Google's *Rich Snippet Testing Tool*.

```
Item
   Type: http://schema.org/Person
   name = John Doe
   jobTitle = graduate research assistant
   affiliation = University of Dreams
   additionalName = Johnny
   url = http://www.example.com/~JohnnyD
   address = Item(1)
Item 1
   Type: http://schema.org/PostalAddress
   streetAddress = 1234 Peach Drive
   addressLocality = Warner Robins
   addressRegion = Georgia
```

The same machine-readable terms can be used not only in HTML Microdata, but also in other annotations such as [RDFa](https://en.wikipedia.org/wiki/RDFa "RDFa") or [JSON-LD](https://en.wikipedia.org/wiki/JSON-LD "JSON-LD") in the markup, or in an external [RDF](https://en.wikipedia.org/wiki/Resource_Description_Framework "Resource Description Framework") file in a serialization such as [RDF/XML](https://en.wikipedia.org/wiki/RDF/XML "RDF/XML"), [Notation3](https://en.wikipedia.org/wiki/Notation3 "Notation3"), or [Turtle](https://en.wikipedia.org/wiki/Turtle_(syntax) "Turtle (syntax)").

## Support

* Servers: [Google](https://en.wikipedia.org/wiki/Google "Google") can use microdata in its [result pages](https://en.wikipedia.org/wiki/Search_engine_results_page "Search engine results page"). It was the preferred snippet format for the [Google+](https://en.wikipedia.org/wiki/Google%2B "Google+") social network.
* Browsers: As of July 2021[[update]](https://en.wikipedia.org/w/index.php?title=Microdata_(HTML)&action=edit), no major browser supports the Microdata [DOM](https://en.wikipedia.org/wiki/Document_Object_Model "Document Object Model") [API](https://en.wikipedia.org/wiki/API "API"). Opera supported it from 11.60 (released in 2011), but since removed its implementation. Firefox removed it in version 49.

---

*Source: [Wikipedia — Microdata (HTML)](https://en.wikipedia.org/wiki/Microdata_(HTML)). Text licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*
