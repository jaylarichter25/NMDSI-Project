"""Hand-curated structure, checked against the PDF text by build_faculty.py.

LISTS: cells that are line-separated lists in the PDF. Each is verified to contain
exactly the same words as the source cell.
TAGS: "Name | tag; tag; tag". Every word of every tag must appear in that person's bio.
"""

LISTS = {
    "Aki Roberts": "Criminology|Criminal Justice|NIBRS|Quantitative Methods|Japan",
    "Aleksandra J. Snowden": "Crime mapping and analysis|GIS",
    "Anne Clough": "Medical Imaging|Mathematical Modeling|Integral Equations",
    "Anthony J. Parolari": "Watershed and urban hydrology|Ecohydrology|Modeling",
    "Chao Zhu": "Applied probability and stochastic processes|Actuarial sciences and finance|Computational linear algebra|Mathematical statistics",
    "Cheng-Han Yu": "Bayesian Computation|Spatiotemporal Modeling|Hierarchical Models|Kernel methods|Neuroimaging",
    "Cristinel Ababei": "Network-on-chip based multicore processors and datacenters (energy, reliability)|Embedded systems (uncertainty, aerial/underwater drones, LiDARs in transportation, IoT)|FPGAs, reconfigurable computing and parallel computing|Distribution networks and smart buildings|Simulation and optimization of vehicle battery packs|Electronic design automation for VLSI and FPGA circuits",
    "David Krause": "Investments and Valuation|Investment Ethics|Portfolio Performance Measurement|Corporate Finance",
    "Debbie Perouli": "Security and privacy of social robots|Distributed ledger (blockchain) technologies|Network protocol design and analysis|Cybersecurity education|Quantum computation and information",
    "Dmitri Babikov": "Anomalous Isotope Effect in Ozone Forming Reaction|Vibrational States Approach to Quantum Computing|Geometric Phase Effect and Spectroscopy of Cyclic-N3 Molecule|Mixed Quantum / Classical Theory|Semi-classical Methodology for Molecular Dynamics|Collision-induced Fragmentation of Small Sodium Clusters|Computer Simulation of the Ribosome|Visualization of the Potential Energy Surfaces",
    "Elaine Spiller": "Mathematical geoscience|Probabilistic hazard mapping|Uncertainty quantification|Stochastic processes and simulations|Data assimilation",
    "Sheikh Iqbal Ahamed": "mHealth|Pervasive/ubiquitous computing|Security, privacy and trust",
    "Jake Luo": "Health Big Data and Predictive Analysis|Natural Language Processing|Health Informatics and Management|Text Mining and Information Extraction|Artificial Intelligence and machine learning",
    "Jeb Willenbring": "Representation Theory|Discrete Mathematics|Mathematical Physics",
    "Jim Pokrywczynski": "Sports marketing|International advertising|Brand tracking on social media",
    "John Roberts": "Social Networks|Quantitative Methods|Mathematical Sociology|Criminology",
    "Jun Zhang": "Image processing and computer vision|Digital signal processing|Digital communications",
    "Kate Rohit": "Natural Language Processing|Machine Learning|Biomedical Informatics|Artificial Intelligence",
    "Majeed Hayat": "Dynamical models for interdependent cyber-physical systems|Signal and image processing|Performance modeling of heterogeneous distributed computing systems|Statistical communication theory|Avalanche photodiodes|High-speed optical receivers|Probability and stochastic processes",
    "Maria Haigh": "Misinformation, Disinformation, Fake News, Big Data, Society|Research on intellectual property issues, role of libraries in transitional Ukrainian society.",
    "Matthew Petering": "Operations research|Discrete event simulation|Math programming|Logistics|Transportation|Ocean and rail container shipping|Material handling systems|Supply chain management|Manufacturing",
    "Mehdi Maadooliat": "Bioinformatics|Machine Learning|Functional Data Analysis and Skewed Distributions",
    "Michael Zimmer": "Privacy|Data ethics|Internet research ethics",
    "Mumin Cebe": "Security for critical infrastructure networks|Security of Internet of Things (IoT)|Blockchain and Data Security|5G Security",
    "Nasim Yahyasoltani": "Statistical Signal Processing and Machine Learning|Artificial Intelligence|Optimization Theory|Network Science and Graph Signal Processing|Data Science",
    "Nathaniel Stern": "Innovation and Entrepreneurship|Product Design and Development|Computer Vision|Interactive Art|Art and Technology|Aesthetics|Affect and Embodiment theory|Sustainable Technologies|Waste and reuse",
    "Naveen Bansal": "Linear Hypothesis in Errors in Variables Model|Ranking and Selection|Bayesian Statistics|Multiple Hypotheses Testing|Gene Expression Data Analysis",
    "Nicholas Jolly": "Labor economics|Applied microeconomics|Job displacement|Disability|Economics of Gender",
    "Patrick McNamara": "Antibiotic Resistance|Micropollutants|Pyrolysis|Residuals and Biosolids",
    "Paul Roebber": "Synoptic and mesoscale meteorology|Climate dynamics|Systems modeling (machine learning, agent-based models)|Forecast verification|Numerical weather prediction",
    "Peter Hinow": "Applied Mathematics|Partial Differential Equations|Mathematical Biology",
    "Praveen Madiraju": "Data Science/Machine Learning: Text Analytics, Text Mining|Healthcare Informatics: Behavioral Informatics, Machine Learning Applications for Healthcare, Mobile Applications|Databases and BigData : Social Media (Twitter) Analysis, Data Analytics, NoSQL Systems, Personalization, Global Constraint Checking and Querying in Multidatabases, XML Databases, Constraints in XML Databases",
    "Priya Nambisan": "Social Media and impact on mental well-being|Aging research and digital technologies|Health Care Innovation & Entrepreneurship|Consumer/Patient Experience in Digital Environments",
    "Richard J. Povinelli": "Machine Learning|Signal Processing|Dynamical Systems and Chaos",
    "Sabirat Rubya": "Human-computer interaction|Social Computing|Health Informatics|Human-aided Machine Learning",
    "Said Audi": "Acute lung injury, acute respiratory distress syndrome (ARDS)|Lung Transplantation|Pulmonary endothelium metabolism, pulmonary hemodynamics|Computational modeling|Functional imaging (SPECT, optical)",
    "Taly Gilat-Schmidt": "Medical imaging systems|Computed tomography|Image reconstruction",
    "Thomas Schwarz": "Scalable Distributed Data Structures|Large Scale Storage Systems|High Availability, Erasure Correcting Codes|Security",
    "Vytaras Brazauskas": "Actuarial Science|Quantitative Risk Management|Robust Statistics",
    "Walter Bialkowski": "Epidemiology|Healthcare analytics|Data science|Community participatory research",
    "Wilkistar Otieno": "Predictive Data Analytics for Manufacturing Systems|Sustainable Manufacturing (Remanufacturing)|Energy Sustainability|Reliability Analysis of Products and Systems|Engineering Education",
    "Zeyun Yu": "Image processing and analysis|3D geometric modeling and visualization|Scientific Computing in Biomedicine",
}

_TAGS = """
Ai Bo | Substance use prevention; Survey research; Evidence synthesis; Machine learning
Aki Roberts | Criminology; Criminal justice; NIBRS; Quantitative methods; Japan
Aleksandra J. Snowden | Crime mapping; GIS
Alexander Dijo | Technology development; Digital transformation; Artificial intelligence
Alita Burmeister | Molecular microbiology; Evolution
Amir A. Alwan | Decision making under uncertainty; Queueing theory; Reinforcement learning; Dynamic pricing; Supply chain management
Amit Bhatnagar | E-commerce; Multimedia advertising; Information search; Customer satisfaction
Amol Mali | Artificial intelligence; Data science; Internet of Things
Andrew G. Meyer | Environmental education; Behavioral economics
Anne Clough | Medical imaging; Mathematical modeling; Integral equations
Anthony J. Parolari | Urban hydrology; Ecohydrology; Modeling
Arjun Saha | Drug discovery; AI; Computational chemistry; Biophysics
Avik Chakrabarti | International trade; International finance; Industrial organization; Economic systems; Outsourcing
Ayesha Siddika Nipu | Natural language processing; Machine learning; Healthcare outcomes; Transformers; Trustworthy AI
Badar Al Lawati | Internet of Things; Artificial intelligence; Digital payments; Video games
Bhagwant Sindhu | Upper extremity rehabilitation; Rehabilitation assessments; Rehabilitation outcomes
Bin Wang | International finance; Investments
Bing Yu | Optical imaging; Spectroscopy; Cancer detection; Global health
Brooke Slavens | Rehabilitation engineering; Musculoskeletal biomechanics
Changshan Wu | Remote sensing; Geographic information science; Spatial data analysis
Chao Zhu | Applied probability; Stochastic processes; Actuarial sciences; Computational linear algebra; Mathematical statistics
Charles Franklin | Political races; Public policy
Chelsea Cook | Social behavior
Cheng-Han Yu | Bayesian computation; Spatiotemporal modeling; Hierarchical models; Kernel methods; Neuroimaging
Chris Marshall | Antimicrobial resistance; Biogeochemical cycling
Chudamani Poudyal | Actuarial data science; Big data analytics; Computational statistics; Statistical learning; Stochastic optimization
Clark Evans | Atmospheric science
Colleen Galambos | Care transitions; End of life decision making; Aging in place; Long-term care; Gerontechnology
Cristinel Ababei | Multicore processors; Embedded systems; FPGAs; Parallel computing; Smart buildings; Electronic design automation
Daniel Cirkovic | Random networks; Extreme value theory; Social media; Bayesian statistics
Daniel Gervini | Statistics
Darren Wheelock | Criminal punishment; Social control; Ethnic inequality; Racial attitudes; Prisoner reentry
David Krause | Investments; Valuation; Portfolio performance; Corporate finance
David Spade | Statistical literacy
David Witzling | Technological approaches to art making
Debbie Perouli | Social robots; Blockchain; Network protocol design; Cybersecurity education; Quantum computation
Deepak Babu | Information technology; Management
Derek Nazareth | Heuristic optimization; Social media analysis; Medical data ethics
Dietmar Wolfram | Bibliometrics; Scholarly communication; Information retrieval; User studies
Dmitri Babikov | Quantum computing; Molecular dynamics; Computer simulation; Spectroscopy; Potential energy surfaces
Edward Blumenthal | Genetic; Molecular; Physiological/behavioral
Edward F Levitas | Strategic management; Innovation
Elaine Spiller | Mathematical geoscience; Hazard mapping; Uncertainty quantification; Stochastic processes; Data assimilation
Elsbeth Kalenderian | Informatics; Patient safety; Quality improvement; Dental setting
Emily Latch | Ecological processes; Evolutionary trajectory
Emily Cramer | Health communication; Disparities
Erin Ruppel | Communication technologies; Interpersonal communication; Health communication; Small group communication
Ethan Schmick | Economic history; Labor economics; Economics of education
Gabriel Velez | Educational experiences; Identity development
Gerry Canavan | Science fiction; Utopia
Giorgo Sertsios | Corporate finance; Economics; Econometrics
Henry Duah | Social determinants of health; Opioid use disorder; Big data; Population health; Machine learning
Hunter Sandidge | Automated data science; Agentic AI
Hyunkyoung Oh | Digital health technologies; Chronic conditions; Natural language processing; Machine learning; Artificial intelligence
Inga Wang | Stroke rehabilitation; Aging research; Rehabilitation outcomes
Sheikh Iqbal Ahamed | mHealth; Ubiquitous computing; Security; Privacy
Itzi Lazkano | Innovation economics; Environmental economics; Energy economics
J. Dietenberger | Information technology; Project management; Organizational development
Jacklynn Fitzgerald | Neuroanatomy; Posttraumatic stress disorder; Emotion dysregulation
Jacob Rice | Automated assembly; Robotic solutions; Control solutions
Jake Luo | Health big data; Predictive analysis; Natural language processing; Health informatics; Text mining; Machine learning
Jangsu Yoon | Econometric theory; Applied econometrics
Jeanne-Nicole Mellon Saint-Laurent | Syriac studies; Early Christianity; Hagiography; Sacred narrative
Jeb Willenbring | Representation theory; Discrete mathematics; Mathematical physics
Jenna Green | Writing; Multimodality; Student success; Digital composing
Jeremy Lee | Causal inference; Human-computer interaction; Survey methodology; Health care; Financial planning
Jim Pokrywczynski | Sports marketing; International advertising; Brand tracking; Social media
Joan Shapiro Beigh | Individual differences; Teams
John Roberts | Social networks; Quantitative methods; Mathematical sociology; Criminology
Jonah Gaster | Topology
Joseph Retzer | Statistical analysis; Econometric analysis; Marketing models; Bayesian frameworks
Joseph Matthes | Marketing strategy; Franchising; Omnichannel integration; Firm performance
Joseph A. LaManna | Biotic interactions; Environmental change; Ecological disturbances; Ecosystem function; Resilience
Joseph Wall | Accounting fraud; AI ethics; Forensic investigations; Cryptocurrency risks; Disruptive technologies
Jun Zhang | Image processing; Computer vision; Digital signal processing; Digital communications
Kali Murray | Patent law
Kanchan Chowdhury | Machine learning; Database systems; Geospatial analytics; Reinforcement learning; Distributed computing
Karen Andeen | Particle physics; Astroparticle physics
Kate Rohit | Natural language processing; Machine learning; Biomedical informatics; Artificial intelligence
Keith Dookeran | Real-world data; Life-sciences; Epidemiologist
Kevin Trainor | Customer relationship management; Digital marketing; Sales strategy; Marketing education
Kristian O'Connor | Biomechanics; Musculoskeletal injury
Kristof Kipp | Sports science; Biomechanics
Laira Anne Stark | Data science
Larry Zhiming Xu | Emerging media; Information systems; Data science; Computational social science
Laura Roehl | Academics; Research; Data science
Layth Alwan | Supply chain; Operations management; Statistical process control; Forecasting
Lei Fan | Physics-based neural networks; Machine learning; Cardiovascular modeling; Imaging
Lillian Campbell | Rhetoric; Composition; Science and technology studies; Gender studies
Linnea Laestadius | Novel technologies; Health behavior; Policy; Communication
Lisa N. Petrella | Temperature stress; C. elegans
Lu He | Health informatics; Human-computer interaction; Natural language processing; Health disparities
Lynne Knobloch-Fedders | Assessment; Intervention; Couples; Depression; Anxiety
Madhusudan Dey | Protein function; Proteostasis; Protein-misfolding disorders
Majeed Hayat | Cyber-physical systems; Signal processing; Image processing; Distributed computing; Statistical communication theory; Avalanche photodiodes
Margaret Kipp | Social tagging; Metadata; Semantic web; Information retrieval; Classification systems
Maria Haigh | Misinformation; Disinformation; Big data; Intellectual property; Libraries
Maria Goranova | Corporate governance; Shareholder activism; Ownership
Maria Novotny | Rhetoric; Reproductive health technologies; Health advocacy; Infertility
Mark Barratt | Supply chain collaboration; Inventory record accuracy
Mark Schwartz | Plant-climate interactions
Matthew Petering | Operations research; Discrete event simulation; Logistics; Supply chain management; Manufacturing
Matthew Friedel | Applications in AI; Disruptive technologies; Entrepreneurship
Matthew Mleczko | Housing policies; Poverty; Equity; Social cohesion
Mehdi Maadooliat | Bioinformatics; Machine learning; Functional data analysis; Skewed distributions
Mengyun Zhang | Sustainable operations management; Remanufacturing; Closed-loop supply chain
Michael Zimmer | Privacy; Data ethics; Internet research ethics
Michael Nosonovsky | Self-organization; Biomimetic surfaces; Adhesion; Capillary force
Min Wu | Dental informatics; Public health informatics; Clinical informatics; ROC analysis; Human-computer interaction
Min Sook Park | Data science; Health informatics; Knowledge organization; Information behavior
Mohammad Habibur Rahman | Bio-robotics; Wearable robots; Rehabilitation robotics; Exoskeleton robots; Digital twin; Teleoperation
Mumin Cebe | Critical infrastructure security; Internet of Things; Blockchain; Data security; 5G security
N. Kundan Kishor | Macroeconomics; Monetary economics; Time series econometrics
Nadiyah Johnson | Artificial intelligence; Machine learning; Natural language processing
Nasim Yahyasoltani | Statistical signal processing; Machine learning; Artificial intelligence; Optimization theory; Network science; Data science
Nate Lemoine | Climate warming; Plant-herbivore interactions
Nathaniel Stern | Entrepreneurship; Product design; Computer vision; Interactive art; Sustainable technologies
Naveen Bansal | Hypothesis testing; Ranking and selection; Bayesian statistics; Gene expression data analysis
Nicholas Jolly | Labor economics; Applied microeconomics; Job displacement; Disability; Economics of gender
Nicholas J Reiter | RNA sequences; Chromatin-associated proteins
Odai Khasawneh | Technophobia; Technostress; Technology avoidance
Pallav Routh | Customer relationship management; B2B relationship marketing; Sales management; Social network
Patrick McNamara | Antibiotic resistance; Micropollutants; Pyrolysis; Biosolids
Paul Roebber | Mesoscale meteorology; Climate dynamics; Systems modeling; Machine learning; Numerical weather prediction
Paula Papanek | Exercise; Homeostasis; Health and well-being
Peter Dunn | Mating systems; Life history strategies; Population genetics; Threatened species
Peter Hinow | Applied mathematics; Partial differential equations; Mathematical biology
Phoenix Do | Social determinants of health; Health disparities; Residential segregation; Applied econometrics; Policy analysis
Praveen Madiraju | Data science; Machine learning; Text mining; Healthcare informatics; Databases; Social media analysis
Priya Deshpande | Biomedical data integration; Artificial intelligence; Big data analytics; Natural language processing; Information retrieval
Priya Nambisan | Social media; Mental well-being; Aging research; Health care innovation; Patient experience
Purush Papatla | Textual content; Pictorial content; Video content; Audio content
Rani Elhajjar | Composite material systems; Physics-informed neural networks; Experimental mechanics; Digital image correlation; Computer vision
Razia Azen | Dominance analysis; General linear models; Multivariate models
Rebecca Neumann | International finance; Innovation; Financial development
Richard J. Povinelli | Machine learning; Signal processing; Dynamical systems; Chaos
Rina Ghose | Wicked problems; Mixed-method approach; Public participation; Policy interventions
Sabirat Rubya | Human-computer interaction; Social computing; Health informatics; Human-aided machine learning
Said Audi | Acute lung injury; Lung transplantation; Pulmonary hemodynamics; Computational modeling; Functional imaging
Samantha Majhor | Native American literature; Art; Digital sovereignty; Media
Sanjoy Ghose | Market structure analysis; Business analytics; Pricing; Product design
Satish Puri | Parallel and distributed computing; Spatial big data; High-performance computing
Satya Aditya Akundi | Complex systems engineering; Model-based systems engineering; Cyber-physical systems; Digital quality control
Scott Rex | Corporate marketing; Consulting; Small business; Voice and data technologies
Sergey Kravtsov | Surface temperature trends; Decadal climate variability; Atmospheric jet streams
Shana Ponelis | ICTs; Organizational contexts; Sub-Saharan Africa
Shengtong Han | Biostatistics
Somesh Roy | Combustion modeling; Flow modeling; Multiphysics
Stephen J. Guastello | Nonlinear dynamics; Work performance; Occupational safety; Group behavior; Cognitive workload
Susan McRoy | Natural language processing; Information retrieval; User modeling; Artificial intelligence; Dialog systems
Suzanne Boyd | Dynamical systems; Complex variables; Computer-assisted proof
Swapnil Tripathi | Physics; General relativity; Cosmology; Astrophysics
Taly Gilat-Schmidt | Medical imaging; Computed tomography; Image reconstruction
Tanya Joosten | Tech and human behaviors; Organizations; Mixed methods
Thomas Schwarz | Distributed data structures; Storage systems; High availability; Erasure correcting codes; Security
Thomas Holbrook | Political behavior; Campaigns and elections; State politics; Research methods
Thomas Kaczmarek | Data science; Cybersecurity operations
Tian Zhao | Type systems; Type inference; Static analysis; Domain specific programming
Tony Gamble | Developmental processes; Evolutionary processes; Biological diversity
Vytaras Brazauskas | Actuarial science; Quantitative risk management; Robust statistics
Walter Bialkowski | Epidemiology; Healthcare analytics; Data science; Community participatory research
Walter McDonald | Urban water systems; Monitoring; Modeling
Wan-Chen Lee | Metadata; Data curation; Knowledge organizations; Culture
Wilkistar Otieno | Predictive data analytics; Sustainable manufacturing; Energy sustainability; Reliability analysis; Engineering education
Woonsup Choi | Climate change; Urbanization; Land use change; Hydrology; Water quality
Xiangming Mu | Information retrieval; User behavior; Health informatics; Social semantics; Text mining
Xiaohan Yan | Research data management
Xin Luo | Corporate disclosure; Executive compensation; Investment efficiency; Textual analysis
Yuanyuan (April) Song | Theory Research Exchange (T-Rex); Digitizing knowledge; Analytics
Zeyun Yu | Image processing; 3D geometric modeling; Scientific computing; Biomedicine
Zhen Zeng | AI security; Distributed systems
"""

TAGS = {}
for _line in _TAGS.strip().splitlines():
    _name, _tags = _line.split(" | ")
    TAGS[_name] = [t.strip() for t in _tags.split(";")]
