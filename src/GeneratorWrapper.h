/* ***** BEGIN GPL LICENSE BLOCK *****
 *
 * This file is part of PyOpenNI.
 *
 * PyOpenNI is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * PyOpenNI is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with PyOpenNI.  If not, see <http://www.gnu.org/licenses/>.
 *
 * PyOpenNI is Copyright (C) 2011, Xavier Mendez (jmendeth).
 * OpenNI Python Wrapper (ONIPY) is Copyright (C) 2011, Gabriele Nataneli (gamix).
 *
 * ***** END GPL LICENSE BLOCK ***** */


#ifndef GENERATOR_WRAPPER_H
#define	GENERATOR_WRAPPER_H

#include <XnCppWrapper.h>

void Generator_StartGenerating_wrapped(xn::Generator& self);
void Generator_StopGenerating_wrapped(xn::Generator& self);

void Generator_WaitAndUpdateData_wrapped(xn::Generator& self);

XnBool Generator_IsGenerating_wrapped(xn::Generator& self);
void Generator_SetGenerating(xn::Generator& self, XnBool value);

XnBool Generator_IsDataNew_wrapped(xn::Generator& self);

#endif	/* GENERATOR_WRAPPER_H */
