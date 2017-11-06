# ArchivesSpace Beyond the Basics Skillshare: Data Auditing for the ArchivesSpace PUI

In August 2017, Yale University Libraries' special collections repositories initiated a library-wide project in preparation for the rollout of the ArchivesSpace Public User Interface (PUI) in early 2018. The project is comprised of six subgroups focusing on different aspects of the implementation:
- Accessibility
- User experience and design
- Technical integrations
- Training and documentation
- Branding and promotion
- Data cleanup and enhancements (that's us!)

Yale's special collections repositories create an enormous amount of metadata, and the ArchivesSpace PUI represents a radical change from our current finding aid database ([YFAD](http://drs.library.yale.edu/fedoragsearch/rest)). Among other things, this means that we have a lot of data clean-up work to do before we can "go live" with the PUI. The Data Cleanup and Enhancements Workgroup has been charged with identifying the nature and extent of our data problems, and coming up with in-house or outsourced solutions.

In our initial meetings, we identified a [laundry list](http://addlink.com) of things that could be fixed. But, given the short-term nature of this project, we've had to do some hard thinking about which of our data quality issues will have the greatest impact on our users and on the security of our restricted metadata (i.e. student records, donor-imposed restrictions) once the PUI is implemented, and to stay focused on just those issues. 

Our first task, after narrowing the scope of our work, was to identify the nature and extent of our problems in each of the eight areas on which we decided to focus:
  - Publication status
  - Restrictions
  - Dates
  - Shared records/controlled value lists + Extents
  - Note Labels
  - Preferred Citations
  - URLs
  - Containers

The demos that follow outline the steps we took to audit our data in each of these areas. We share them in the hopes that they can be of use to other institutions seeking to undertake similar work. We will continue to update this repository as we evaluate our results and implement our solutions.

### Requirements

- ArchivesSpace 2.x+
- MySQL client
- Python 3
  - Highly Recommended: [Anaconda](https://www.anaconda.com/download/) (Python distribution and package manager)
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
- Returns note text (JSON format), publication status, parent URI, and persistent ID

`get_component_pub_status.sql`
- Returns archival object publication status, arcihival object display string, archival object level, parent resource publication status, parent EAD ID, and URI

`get_resource_pub_status.sql`
- Returns resource title, EAD ID, publication status, and URI

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
- Returns URI, JSON-formatted note text, restriction note type, local restriction type, restriction begin date, restriction end date, title(s), persistent ID

`get_use_restricts.sql`
- Returns URI, JSON-formatted note text, restriction note type, local restriction type, restriction begin date, restriction end date, title(s), persistent ID

#### Extract Text

`extract_restricts.py`

Extracts restriction note text from JSON output from database

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

`accession_dates.sql`
- Returns accession title, URI, date expression, begin date, end date, date type, date label, date certainty, date calendar, date era

`resource_dates.sql`
- Returns resource title, identifier, URI, EAD ID, date expression, begin date, end date, date type, date label, date certainty, date calendar, date era

`component_dates.sql`
- Returns archival object title, archival object URI, parent resource title, parent URI, parent EAD ID, component level, date expression, begin date, end date, date type, date label, date certainty, date calendar, date era. Also can be limited by repository ID and by amount of records. 


#### Analyze Results

`archival_object_date_expression`
- Returns archival object id, archival object title, parent resource record title, EAD ID, resource identifier, repository ID, date expression, date begin, and date end. Limits returns to records where date expression has data and empty machine-readable begin and end dates. Can also be limited by repository ID, and with limits for amount of records to return.

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

### Demo 4: Managing Shared Records (Controlled Value Lists, Agents, Subjects, Container Profiles, etc) + Extents

#### Objectives
- Query the ArchivesSpace database to retrieve all records linked to controlled values
- Analyze results
- Prepare for updates

#### Query Database

`extents_linked_recs.sql`
- Returns

`agents_linked_recs.sql`
- Returns

`subjects_linked_recs.sql`
- Returns

`container_profiles_linked_recs.sql`
- Returns

`get_extents.sql`
- Returns URI, title(s), container summary, etc.

`get_extents_plus_top_containers.sql`
- Returns extent data + container data for comparison

#### Analyze Results

`pandas-toolbox.py`

Group results by physical description, etc.

### Demo 5: Labels

#### Objectives
- Query the ArchivesSpace database to retrieve all user-supplied labels attached to resource-, archival object-, or digital-object level notes.
- Analyze results

#### Query Database

`get_notes.sql`
- Returns note text (JSON format), URI, persistent ID

Note: this query gets all notes. You can run this query one time and run numerous demos from this presentation on the same dataset. Can also split by repository for quicker analysis. Might be a good idea to make copies of the output.

#### Extract Text

`extract_text.py`

Extract notes type and label into a list, along with URI and persistent ID

#### Analyze Data

`pandas-toolbox.py`

Get counts of label usage relative to note type

### Demo 6: Citations

#### Objectives
- Query the ArchivesSpace database to retrieve all preferred citation notes
- Analyze results
- Clean data, prepare for ArchivesSpace update

#### Query Database

`get_notes.sql`
- Returns note text (JSON format), URI, persistent ID

Note: this query gets all notes. You can run this query one time and run numerous demos from this presentation on the same dataset. Can also split by repository for quicker analysis. Might be a good idea to make copies of the output.

#### Extract Text

`extract_text.py`

Extracts text from JSON output.

`ID_missing_call_numbers.py`

Identifies notes which do not contain non-word patterns

#### Clean Data

`insert_call_numbers.py`

Inserts call numbers into preferred citation notes

### Demo 7: URLs

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

### Demo 8: Containers

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
