===========================================
social media links for the res_parter modul
===========================================

.. social media links for the res_parter modul::

This addon is for creating a social media field for the  res_parter module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To get access to the icons in the frontend the res_partner has to have assigned to a company
and under Human resources the work address must be then the the company,username selected for the working address.
You have to do it in order to get access from the backed to the frontend.

.. integration example::

use the fields created on your model based on your needs in your template
for example::

<div class="col-sm-12 text-center" t-if="len(employee_ids)">
    <div t-foreach="employee_ids" t-as="employee" class="col-md-4 mt16 text-center colsize">
        <t t-call="website.publish_management"><t t-set="object" t-value="employee"/></t>
            <a t-att-href="employee.address_id.linkedin" t-if="employee.address_id.linkedin"><i class="fa fa-linkedin"/></a>
            <a t-att-href="employee.address_id.behance" t-if="employee.address_id.behance"><i class="fa fa-behance-square"/></a>
            <a t-att-href="employee.address_id.dribbble" t-if="employee.address_id.dribbble"><i class="fa fa-dribbble"/></a>
            <a t-att-href="employee.address_id.github" t-if="employee.address_id.github"><i class="fa fa-github"/></a>
            <a t-att-href="employee.address_id.google_plus" t-if="employee.address_id.google_plus"><i class="fa fa-google-plus-square"/></a>
            <a t-att-href="employee.address_id.facebook" t-if="employee.address_id.facebook"><i class="fa fa-facebook-square"/></a>
            <a t-att-href="employee.address_id.twitter" t-if="employee.address_id.twitter"><i class="fa fa-twitter"/></a>
    </div>
</div>