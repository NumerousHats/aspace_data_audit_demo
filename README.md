# ArchivesSpace Beyond the Basics Skillshare: Data Auditing for the ArchivesSpace PUI

In August 2017, Yale University Libraries' special collections repositories initiated a library-wide project in preparation for the early 2018 rollout of the ArchivesSpace Public User Interface (PUI). The project is comprised of six subgroups focusing on different aspects of the implementation:
- Accessibility
- User experience and design
- Technical integrations
- Training and documentation
- Branding and promotion
- Data cleanup and enhancements (that's us!)

The sheer quantity of metadata created across YUL special collections, and the extent to which the PUI is a departure from the current finding aid database, [YFAD](http://drs.library.yale.edu/fedoragsearch/rest), means that we will need to perform significant clean-up before the rollout.

But before we can get into cleaning and enhancing our data, we must identify the nature and extent of our problems.

These demos highlight the steps we took (and are still taking) to evaluate and clean our data

### Requirements

- ArchivesSpace 2.x+
- MySQL client
- Python 3
  - [Anaconda](https://www.anaconda.com/download/)
  - `pandas` module (included with Anaconda)
  - `dateutil` module (included with Anaconda)
- [OpenRefine](http://openrefine.org/download.html)
- [LibreOffice](https://www.libreoffice.org/download/download/) or Excel

### Demo 1: Publication Status

#### Objectives 
- Query the ArchivesSpace database to find the publication status of accessions, resources, archival objects, and notes.       
- Analyze results
- Prepare for ArchivesSpace update
  
#### Query Database

`get_note_pub_status.sql`

`get_component_pub_status.sql`

`get_resource_pub_status.sql`

Return URI, publication status (1 is published, 0 is unpublished), title(s)

#### Analyze Results

`pub_status_grouped.sql`

`pandas-toolbox.py`

#### Prepare Data for ArchivesSpace Update

### Demo 2: Access Restrictions

#### Objectives 
  - Query the ArchivesSpace database to retrieve all conditions governing access and conditions governing use notes for resources, archival objects, and digital objects. 
  - Analyze results
  - Clean data, prepare for ArchivesSpace update
  - Troubleshoot errors

#### Query Database

`get_access_restricts.sql`

`get_use_restricts.sql`

Return URI, JSON-formatted note text, restriction note type, local restriction type, restriction begin date, restriction end date, title(s), persistent ID

#### Extract Text

`extract_restricts.py`

Extracts restriction note text from JSON output

`in_need_of_mars.py`

Identifies notes which contain dates or restrictions in free text fields, but do not have machine-actionable restrictions.

#### Analyze and Clean Data in OpenRefine

###### Faceting and Filtering 

###### Regular expressions to find dates in strings:
  - `[^a-zA-z0-9]\d\d\d\d[^a-zA-Z0-9]`
    - Broadest formulation, will return all 4 digit numbers directly in between any 2 non-letter, non-number characters. Will also return accession numbers which contain years
    
###### Reg Ex/OpenRefine Resources:
  - [Reg Ex Checker](https://regex101.com/)
  - [OpenRefine Cheat Sheet](http://arcadiafalcone.net/GoogleRefineCheatSheets.pdf) (Arcadia Falcone)

#### Prepare Data for ArchivesSpace Update

##### Adding columns in OpenRefine

#### Troubleshooting

The rights restriction tables in the ArchivesSpace database are less-than-intuitive, and documentation is lacking. These scripts explicate the differences between result sets and identify duplicates, and may help identify the cause of inconsistent results.

`find_diffs.py`

`find_dupes.py`
 
### Demo 3: Dates

#### Objectives
  - Query the ArchivesSpace database to return all dates for accessions, resources, archival objects, and digital objects.  
  - Analyze results
  - Clean data, prepare for ArchivesSpace update

#### Query Database

`get_accession_dates.sql`

`get_resource_dates.sql`

`get_component_dates.sql`

`get_digital_object_dates.sql`

Return URI, date expression, date type, era, begin date, end date, ... . If an object does not have one of these values NULL is returned.

#### Analyze Results

`dates_w_expression_no_beginend.sql`

Returns all dates that have an expression but no structured begin or end date

`pandas-toolbox.py`

Analyzes date type usage, era, certainty, etc.

##### OpenRefine
- 

#### Prepare Data for ArchivesSpace Update

##### [Timetwister](https://github.com/alexduryee/timetwister) + `subprocess` module
 
  - Thanks to Alex Duryee!

`timetwister_parse.py`

Loops through a spreadsheet containing unstructured data expressions and parses them into machine-readable dates using timetwister

##### `dateutil.parser` module

`date_parse.py`
 
Loops through a spreadsheet containing unstructured data expressions and parses them into machine-readable dates using dateutil Python module

Much less effective than timetwister, but does not require installation of Ruby or timetwister

### Demo 4: Labels

#### Objectives
- Query the ArchivesSpace database to retrieve all user-supplied labels attached to resource-, archival object-, or digital-object level notes.
- Analyze results

#### Query Database

`get_notes.sql`

Gets all notes. Can retrieve this one time and run numerous demos from this presentation on the same dataset. Can also split by repository for quicker analysis.

Returns note text, URI, persistent ID, 

#### Extract Text

`extract_text.py`

Extract notes type and label into a list, along with URI and persistent ID

#### Analyze Data

`pandas-toolbox.py`

Get counts of label usage relative to note type

### Demo 5: URLs

#### Objectives
- Query ArchivesSpace database to retrieve URLs attached to digital objects and notes
- Test validity of links

#### Query Database

Thanks to Youn Noh for her work on this portion of the demo

#### Analyze Data

Thanks to Youn Noh for her work on this portion of the demo

`notes.py`

`check_url.py`

Checks whether a link is active or broken

`digital_object_id.py`

`file_uri.py`

### Demo 6: Containers

### Demo 7: Extents

#### Objectives
- Query the ArchivesSpace database to retrieve all extent statements
- Analyze results
- Clean data, prepare for ArchivesSpace update

#### Query Database

`get_extents.sql`

Returns URI, title(s), container summary, etc.

`get_extents_plus_top_containers.sql`

Returns extent data + container data for comparison

#### Analyze Results

`pandas-toolbox.py`

Group results by physical description, etc.

#### Clean Data

### Demo 8: Citations

#### Objectives
- Query the ArchivesSpace database to retrieve all preferred citation notes
- Analyze results
- Clean data, prepare for ArchivesSpace update

#### Query Database

`get_notes.sql`

Gets all notes. Can retrieve this one time and run numerous demos from this presentation on the same dataset. Can also split by repository for quicker analysis.

Returns resource identifier, note text in JSON format

#### Extract Text

`extract_text.py`

Extracts text from JSON output.

`ID_missing_call_numbers.py`

Identifies notes which do not contain non-word patterns

#### Clean Data

`insert_call_numbers.py`

Inserts call numbers into preferred citation notes

### Demo 9: Managing Shared Records: Controlled Value Lists, Agents, Subjects, Container Profiles, etc.

#### Objectives
- Query the ArchivesSpace database to retrieve all records linked to controlled values
- Analyze results

#### Query Database

`extents_linked_recs.sql`

`agents_linked_recs.sql`

`subjects_linked_recs.sql`

`container_profiles_linked_recs.sql`

Return URI, 

#### Analyze Results

### Lessons Learned

- Prioritize tasks by potential impact on users, data security
- Clean-up is an iterative process
- Use SQL to retrieve data
- Use Python to manipulate, analyze, and update data
  - Output as input

### Next Steps

- Evaluation by repositories
- Finish writing and testing update scripts
- Add update scripts to data_cleanup_workgroup repository
- Agents and Subjects Task Force Work

