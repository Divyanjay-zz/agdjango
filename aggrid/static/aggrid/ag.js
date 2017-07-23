var selectedCount= "";
var columnDefs = [
                        { headerName: "date", field: "date",filter : 'date',filterParams:{
                            comparator:function (filterLocalDateAtMidnight, cellValue){
                                var dateAsString = cellValue;
                                var dateParts = dateAsString.split("/");
                                var cellDate = new Date(Number(dateParts[2]),Number(dateParts[1]) - 1, Number(dateParts[0]));
                                if ( filterLocalDateAtMidnight.getTime() == cellDate.getTime()){
                                    return 0
                                }

                                if (cellDate < filterLocalDateAtMidnight ){
                                    return -1;

                                }

                                if (cellDate > filterLocalDateAtMidnight){
                                    return 1;
                                }
                                }

                            }
                        },



                        {headerName: 'id', field: 'id',valueGetter: function(params){
                            if (selectedCount =="id"){
                                return params.data.id;
                            }
                            else {

                            return params.data.cg_fees;
                        }}
                        }                    
                    ];

var gridOptions = {
                    floatingFilter:true,
                    columnDefs: columnDefs,
                    enableFilter:true,
                    dateComponent: MyDateEditor
                    };
                
                function MyDateEditor(){
                }
                MyDateEditor.prototype.init = function(params) {
                    this.eGui = document.createElement('div');
                    this.eGui.innerHTML = '<input class="myDateWidget" type ="text"/>';
                    this.eInput = this.eGui.querySelectorAll('input')[0];
                    this.listener = params.onDateChanged;
                    this.eInput.addEventListener('input',this.listener);
                    var that = this;
                    $(this.eInput).datepicker({
                        dateFormat: 'dd-mm-yy',
                        altField: '#thealtdate',
                        altFormat: 'yy-mm-dd',
                        onSelect: function() {
                            that.listener();
                        }
                    });
                };

                MyDateEditor.prototype.getGui = function(){
                    return this.eGui;
                };

                MyDateEditor.prototype.getDate =function(){
                    return $(this.eInput).datepicker( "getDate" );

                };

                MyDateEditor.prototype.setDate =function(date){
                    $(this.eInput).datepicker( "setDate" , date );
                };


                MyDateEditor.prototype.destroy =function(){
                    this.eInput.removeEventListener('input',this.listener)
                };

                MyDateEditor.prototype.afterGuiAttached = function(){
                    $('#ui-datepicker-div   ').click(function(e){
                        e.stopPropagation();
                    });
                };

                function onFilterChanged(value) {
                    gridOptions.api.setQuickFilter(value);
                }



(function(){
            $(document).ready(function(){
                var gridDiv = document.querySelector('#myGrid');
                
                new agGrid.Grid(gridDiv, gridOptions);
                var getData = $.ajax('/aggrid/agdu/');                  
                getData.then(function(response, statusText, xhrObj){
                    
                    console.log(xhrObj);
                    
                    gridOptions.api.setRowData(response.data);
                }, 
                function(xhrObj, textStatus, err){
                    console.log(err);
                })
               document.querySelector('#id').addEventListener('click',function(){
                selectedCount = "id";
                gridOptions.api.refreshView();
               });
               document.querySelector('#cg_fees').addEventListener('click',function(){
               selectedCount = "cg_fees";
                gridOptions.api.refreshView();
               });
 
            })            
        })(); 