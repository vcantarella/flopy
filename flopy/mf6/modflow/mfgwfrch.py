from .. import mfpackage
from ..data import mfdatautil


class ModflowGwfrch(mfpackage.MFPackage):
    """
    ModflowGwfrch defines a rch package within a gwf6 model.

    Attributes
    ----------
    fixed_cell : (fixed_cell : keyword)
        indicates that recharge will not be reassigned to a cell underlying the cell specified in the list if the specified cell is inactive.
    auxiliary : [(auxiliary : string)]
        defines an array of one or more auxiliary variable names. There is no limit on the number of auxiliary variables that can be provided on this line; however, lists of information provided in subsequent blocks must have a column of data for each auxiliary variable name defined here. The number of auxiliary variables detected on this line determines the value for naux. Comments cannot be provided anywhere on this line as they will be interpreted as auxiliary variable names. Auxiliary variables may not be used by the package, but they will be available for use by other parts of the program. The program will terminate with an error if auxiliary variables are specified on more than one line in the options block.
    auxmultname : (auxmultname : string)
        name of auxiliary variable to be used as multiplier of recharge.
    boundnames : (boundnames : keyword)
        keyword to indicate that boundary names may be provided with the list of recharge cells.
    print_input : (print_input : keyword)
        keyword to indicate that the list of recharge information will be written to the listing file immediately after it is read.
    print_flows : (print_flows : keyword)
        keyword to indicate that the list of recharge flow rates will be printed to the listing file for every stress period time step in which ``BUDGET PRINT'' is specified in Output Control. If there is no Output Control option and PRINT\_FLOWS is specified, then flow rates are printed for the last time step of each stress period.
    save_flows : (save_flows : keyword)
        keyword to indicate that recharge flow terms will be written to the file specified with ``BUDGET FILEOUT'' in Output Control.
    ts_filerecord : [(ts6 : keyword), (filein : keyword), (ts6_filename : string)]
        ts6 : keyword to specify that record corresponds to a time-series file.
        filein : keyword to specify that an input filename is expected next.
        ts6_filename : defines a time-series file defining time series that can be used to assign time-varying values. See the ``Time-Variable Input'' section for instructions on using the time-series capability.
    obs_filerecord : [(obs6 : keyword), (filein : keyword), (obs6_filename : string)]
        filein : keyword to specify that an input filename is expected next.
        obs6 : keyword to specify that record corresponds to an observations file.
        obs6_filename : name of input file to define observations for the Recharge package. See the ``Observation utility'' section for instructions for preparing observation input files. Table obstype lists observation type(s) supported by the Recharge package.
    maxbound : (maxbound : integer)
        integer value specifying the maximum number of recharge cells cells that will be specified for use during any stress period.
    periodrecarray : [(cellid : integer), (recharge : double), (aux : double), (boundname : string)]
        cellid : is the cell identifier, and depends on the type of grid that is used for the simulation. For a structured grid that uses the DIS input file, cellid is the layer, row, and column. For a grid that uses the DISV input file, cellid is the layer and cell2d number. If the model uses the unstructured discretization (DISU) input file, then cellid is the node number for the cell.
        recharge : is the recharge flux rate ($LT^{-1$). This rate is multiplied inside the program by the surface area of the cell to calculate the volumetric recharge rate. A time-series name may be specified.
        aux : represents the values of the auxiliary variables for each recharge. The values of auxiliary variables must be present for each recharge. The values must be specified in the order of the auxiliary variables specified in the OPTIONS block. If the package supports time series and the Options block includes a TIMESERIESFILE entry (see the ``Time-Variable Input'' section), values can be obtained from a time series by entering the time-series name in place of a numeric value.
        boundname : name of the recharge cell. boundname is an ASCII character variable that can contain as many as 40 characters. If boundname contains spaces in it, then the entire name must be enclosed within single quotes.

    """
    auxiliary = mfdatautil.ListTemplateGenerator(('gwf6', 'rch', 'options', 'auxiliary'))
    ts_filerecord = mfdatautil.ListTemplateGenerator(('gwf6', 'rch', 'options', 'ts_filerecord'))
    obs_filerecord = mfdatautil.ListTemplateGenerator(('gwf6', 'rch', 'options', 'obs_filerecord'))
    periodrecarray = mfdatautil.ListTemplateGenerator(('gwf6', 'rch', 'period', 'periodrecarray'))
    package_abbr = "gwfrch"

    def __init__(self, model, add_to_package_list=True, fixed_cell=None, auxiliary=None, auxmultname=None,
                 boundnames=None, print_input=None, print_flows=None, save_flows=None,
                 ts_filerecord=None, obs_filerecord=None, maxbound=None, periodrecarray=None,
                 fname=None, pname=None, parent_file=None):
        super(ModflowGwfrch, self).__init__(model, "rch", fname, pname, add_to_package_list, parent_file)        

        # set up variables
        self.fixed_cell = self.build_mfdata("fixed_cell", fixed_cell)

        self.auxiliary = self.build_mfdata("auxiliary", auxiliary)

        self.auxmultname = self.build_mfdata("auxmultname", auxmultname)

        self.boundnames = self.build_mfdata("boundnames", boundnames)

        self.print_input = self.build_mfdata("print_input", print_input)

        self.print_flows = self.build_mfdata("print_flows", print_flows)

        self.save_flows = self.build_mfdata("save_flows", save_flows)

        self.ts_filerecord = self.build_mfdata("ts_filerecord", ts_filerecord)

        self.obs_filerecord = self.build_mfdata("obs_filerecord", obs_filerecord)

        self.maxbound = self.build_mfdata("maxbound", maxbound)

        self.periodrecarray = self.build_mfdata("periodrecarray", periodrecarray)


